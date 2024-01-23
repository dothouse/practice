import pandas as pd
import numpy as np


from flask import Blueprint, render_template, request, url_for, session, g, flash, redirect

from haversine import haversine

from werkzeug.utils import redirect

from sqlalchemy import func

from jeju import db

from jeju.models import TestData, selectData, Pension, Mart, Police, Parm, Hospital, Bank, Tour, Food, Gift


bp = Blueprint('select', __name__, url_prefix='/select')



@bp.route('/select3', methods=('GET', 'POST'))
def show_select3():

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]

    # query filtering
    selected_query = db.session.query(Pension)
    if select_value.pet == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%반려동물%'))
    if select_value.pool == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%수영장%'))
    if select_value.garden == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%마당%'))
    if select_value.sea == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%바다%'))
    if select_value.nocost == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%관리비 없음%'))
    if select_value.bus == 1:
        selected_query = selected_query.filter(Pension.ammen.like('%대중교통%'))
    result_query = selected_query.all()

    # query filtering method 2
    # fil_con1 = and_(TestData.type == 1, pension.ammen.like('%반려동물%'), pension.ammen.like('%대중교통%'))
    # type1 = db.session.query(TestData).join(pension, pension.pensionID == TestData.pensionID).filter(fil_con1).all()

    # 필터링된 pensionID 만 리스트로 이를 다시 필터로 만들어서 사용
    # in_ 는 list랑 결합해서 사용
    # result_pensionID_list = [item.pensionID for item in result_query]

    # type1 = (db.session.query(TestData).join(pension, TestData.pensionID == pension.pensionID)
    #          .filter(TestData.type == 1).filter(pension.pensionID.in_(result_pensionID_list)).all())

    ### 점수 계산하기

    pension_data = db.session.query(Pension).all()
    mart_data = db.session.query(Mart).all()

    temp_location = (mart_data[0].lat, mart_data[0].lng)
    pension_location = (pension_data[0].latitude, pension_data[0].longitude)

    test_haver = haversine(temp_location, pension_location)

    km = []
    for j in range(len(pension_data)):
        cnt = 0
        pension_name = pension_data[j].pensionID
        for i in range(len(mart_data)):
            start = (mart_data[i].lat, mart_data[i].lng)
            goal = (pension_data[j].latitude, pension_data[j].longitude)
            haver = haversine(start, goal)
            if haver < 5:
                cnt +=1
        km.append([pension_name, cnt])

    # 선택값이 없는 테이블 계산
    non_distance = []
    non_table_list = ['Police', 'Hospital', 'Bank',  'Mart', 'Parm', 'Gift']
    for data in non_table_list:
        temp_data = db.session.query(globals()[str(data)]).all()
        for j in range(len(pension_data)):
            cnt = 0
            pensionID = pension_data[j].pensionID
            for i in range(len(temp_data)):
                start = (temp_data[i].lat, temp_data[i].lng)
                goal = (pension_data[j].latitude, pension_data[j].longitude)
                haver = haversine(start, goal)
                if data == 'Mart':
                    bound = 5
                elif data == 'Police':
                    bound = 20
                elif data == 'Bank':
                    bound = 10
                elif data == 'Hospital':
                    bound = 3
                elif data == 'Parm':
                    bound = 3
                elif data == 'Gift':
                    bound = 10
                if haver < bound:
                    cnt += 1
            non_distance.append([pensionID, cnt, data, bound])

    # 선택값이 있는 테이블 계산
    yes_distance = []
    table_list = [('Tour', select_value.spot2), ('Food', select_value.food)]
    for data, selected in table_list:
        temp_data = db.session.query(globals()[str(data)])
        if ((data == 'Tour') & ((selected % 10) == 1) ):
            temp_data2 = temp_data.filter((globals()[str(data)].detailtype == selected) | (globals()[str(data)].detailtype == selected + 2)).all()
        elif ((data == 'Tour') & ((selected % 10) == 2)) :
            temp_data2 = temp_data.filter((globals()[str(data)].detailtype == selected) | (globals()[str(data)].detailtype == selected + 2)).all()
        else :
            temp_data2 = temp_data.filter(globals()[str(data)].detailtype == selected).all()
        for j in range(len(pension_data)):
            cnt = 0
            pensionID = pension_data[j].pensionID
            for i in range(len(temp_data2)):
                start = (temp_data2[i].lat, temp_data2[i].lng)
                goal = (pension_data[j].latitude, pension_data[j].longitude)
                haver = haversine(start, goal)
                bound = 10
                if haver < bound:
                    cnt += 1
            yes_distance.append([pensionID, cnt, data, bound])

    count_list = non_distance + yes_distance

    df_count = pd.DataFrame(count_list)
    df_count.columns = ['pensionID', 'cnt', 'data', 'bound']

    def cal_outlier(df):
        temp = df['cnt']

        IQR = temp.quantile(0.75) - temp.quantile(0.25)
        Q3 = temp.quantile(0.75)
        Q1 = temp.quantile(0.25)

        df_temp = pd.DataFrame(temp[(temp > (Q3 + (1.5 * IQR))) | (temp < (Q1 - (1.5 * IQR)))])
        df_temp.columns = ['cnt']

        return df_temp['cnt'].to_list()


    data_list = ['Police', 'Hospital', 'Bank', 'Mart', 'Parm', 'Gift', 'Tour', "Food"]
    outlist = []
    for data_name in data_list:
        temp = df_count[df_count['data'] == data_name]
        df_temp = df_count[df_count['cnt'].isin(cal_outlier(temp))]
        outlist.extend(df_temp['pensionID'].unique())
    
    # 이상치가 제거된 새로운 타입별 df 생성
    for data_name in data_list:
        temp = df_count[~df_count['pensionID'].isin(outlist)]
        globals()['type_' + str(data_name)] = temp[temp['data'] == data_name]

    for data_name in data_list:
        globals()['mean_' + str(data_name)] = np.mean((globals()['type_' + str(data_name)].cnt.values))
        globals()['std_' + str(data_name)] = np.std((globals()['type_' + str(data_name)].cnt.values))


    temp_list = []
    for i in range(len(type_Tour)):
        name = type_Tour.iloc[i,:].pensionID
        for data_name in data_list:
            # z -score
            # (x - mean) / std
            globals()[str(data_name) + '_score'] = round(((globals()['type_'+str(data_name)].iloc[i,:].cnt)
                                                          - globals()['mean_' + str(data_name)]) / globals()['std_' + str(data_name)], 2)
            globals()[str(data_name) + '_cnt'] = (globals()['type_'+str(data_name)].iloc[i,:].cnt)

        score = (Hospital_score * select_value.hospital +
                 Parm_score * select_value.hospital +
                 Mart_score * select_value.mart +
                 Bank_score * select_value.bank +
                 Police_score * select_value.police +
                 Gift_score * select_value.gift +
                 Tour_score +
                 Food_score)

        temp_list.append([name, score,
                          Hospital_score, Parm_score, Police_score, Mart_score, Bank_score, Gift_score, Tour_score, Food_score,
                          Hospital_cnt, Parm_cnt, Police_cnt, Mart_cnt, Bank_cnt, Gift_cnt, Tour_cnt, Food_cnt])

    df_score = pd.DataFrame(temp_list)
    df_score.columns = ['name', 'score', 'hospital', 'parm', 'police', 'mart', 'bank', 'gift', 'tour', 'food',
                                        'hospital_cnt', 'parm_cnt', 'police_cnt', 'mart_cnt', 'bank_cnt', 'gift_cnt', 'tour_cnt', 'food_cnt']
    df_score.sort_values(by='score', ascending=False, inplace=True)
    score_list = df_score['score'].sort_values(ascending=False)

    # score1, score2, score3 = score_list.unique().head(3).values - ndarray는 head가 불가능해서
    if len(score_list.unique()) == 1:
        score1 = score_list.unique()[0].tolist()
        pension1_score, pension1_chk = df_score[df_score['score'] == score1], 1
        pension2_score, pension2_chk = 'none', 0
        pension3_score, pension3_chk = 'none', 0

    elif len(score_list.unique()) == 2:
        score1, score2 = score_list.unique()[0:2].tolist()
        pension1_score, pension1_chk = df_score[df_score['score'] == score1], 1
        pension2_score, pension2_chk = df_score[df_score['score'] == score2], 1
        pension3_score, pension3_chk = 'none', 0
    else:
        score1, score2, score3 = score_list.unique()[0:3].tolist()
        pension1_score, pension1_chk = df_score[df_score['score'] == score1], 1
        pension2_score, pension2_chk = df_score[df_score['score'] == score2], 1
        pension3_score, pension3_chk = df_score[df_score['score'] == score3], 1


    # for i in range(1, 4):
    #     if globals()['pension' + str(i) + '_chk'] == 1:
    #         globals()['pension' + str(i) + '_name'] = globals()['pension' + str(i) + '.name.values'][0]
    #         globals()['pension' + str(i) + '_detail'] = db.session.query(Pension).filter(Pension.pensionID ==
    #                                                                                      globals()['pension' + str(i) + '_name']).all()[0]
    #     else :
    #         globals()['pension' + str(i) + '_detail'] = 'none'


    if pension1_chk == 1:
        pension1_name = pension1_score.name.values[0]
        pension1_detail = db.session.query(Pension).filter(Pension.pensionID == pension1_name).first()
    else :
        pension1_detail = "none"

    if pension2_chk == 1:
        pension2_name = pension2_score.name.values[0]
        pension2_detail = db.session.query(Pension).filter(Pension.pensionID == pension2_name).first()
    else :
        pension2_detail = "none"

    if pension3_chk == 1:
        pension3_name = pension3_score.name.values[0]
        pension3_detail = db.session.query(Pension).filter(Pension.pensionID == pension3_name).first()
    else :
        pension3_detail = "none"

    return render_template("select/select3.html",
                            result = result_query,
                           test = df_score,
                           pension1_score = pension1_score, pension2_score = pension2_score, pension3_score = pension3_score,
                           pension1_chk =pension1_chk, pension2_chk = pension2_chk, pension3_chk= pension3_chk,
                           pension1_detail = pension1_detail, pension2_detail = pension2_detail, pension3_detail = pension3_detail,
                           non_distance = count_list, test1 = mean_Tour)







