import pandas as pd
from flask import Blueprint, render_template, request, url_for, session, g, flash

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


from werkzeug.utils import redirect

from sqlalchemy import func

from jeju import db

from jeju.models import TestData, selectData, pension


bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/select1')
def open_select1():

    return render_template('select/select1.html')


@bp.route('/select2', methods=('GET', 'POST'))
def show_select2():
    # 카테고리 옵션

    # 유형1
    if request.form['month'] == 'monthType1':
        monthType_str = '한달유형1'
        monthType = 1
    elif request.form['month'] == 'monthType2':
        monthType_str = '한달유형2'
        monthType = 2
    elif request.form['month'] == 'monthType3':
        monthType_str = '한달유형3'
        monthType = 3
    elif request.form['month'] == 'monthType4':
        monthType_str = '한달유형4'
        monthType = 4
    elif request.form['month'] == 'monthType5':
        monthType_str = '한달유형5'
        monthType = 5

    # 관광지
    if request.form['spot1'] == 'spot1Type1':
        spot1Type_str = '관광유형1'
        spot1Type = 1
    elif request.form['spot1'] == 'spot1Type2':
        spot1Type_str = '관광유형2'
        spot1Type = 2
    elif request.form['spot1'] == 'spot1Type3':
        spot1Type_str = '관광유형3'
        spot1Type = 3
    elif request.form['spot1'] == 'spot1Type4':
        spot1Type_str = '관광유형4'
        spot1Type = 4
    elif request.form['spot1'] == 'spot1Type5':
        spot1Type_str = '관광유형5'
        spot1Type = 5

    # var
    # id_spot2_spot2Type1 = ["유형a_1", "유형a_2"];
    # var
    # id_spot2_spot2Type2 = ["유형b_1", "유형b_2"];
    # var
    # id_spot2_spot2Type3 = ["유형c_1", "유형c_2"];
    # var
    # id_spot2_spot2Type4 = ["유형d_1", "유형d_2"];
    # var
    # id_spot2_spot2Type5 = ["유형e_1", "유형e_2"];

    # 여행지 소분류
    if request.form['spot2'] == '유형a_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 11
    elif request.form['spot2'] == '유형a_2':
        spot2Type_str = request.form['spot2']
        spot2Type = 12
    elif request.form['spot2'] == '유형b_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 21
    elif request.form['spot2'] == '유형b_2':
        spot2Type_str = request.form['spot2']
        spot2Type = 22
    elif request.form['spot2'] == '유형c_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 31
    elif request.form['spot2'] == '유형c_2':
        spot2Type_str = request.form['spot2']
        spot2Type = 32
    elif request.form['spot2'] == '유형d_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 41
    elif request.form['spot2'] == '유형d_2':
        spot2Type_str = request.form['spot2']
        spot2Type = 42
    elif request.form['spot2'] == '유형e_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 51
    elif request.form['spot2'] == '유형e_1':
        spot2Type_str = request.form['spot2']
        spot2Type = 52

    # 식당
    if request.form['food'] == 'foodType1':
        foodType_str = '맛집유형1'
        foodType = 1
    elif request.form['food'] == 'foodType2':
        foodType_str = '맛집유형2'
        foodType = 2
    elif request.form['food'] == 'foodType3':
        foodType_str = '맛집유형3'
        foodType = 3
    elif request.form['food'] == 'foodType4':
        foodType_str = '맛집유형4'
        foodType = 4
    elif request.form['food'] == 'foodType5':
        foodType_str = '맛집유형5'
        foodType = 5
    elif request.form['food'] == 'foodType6':
        foodType_str = '맛집유형6'
        foodType = 6
    elif request.form['food'] == 'foodType7':
        foodType_str = '맛집유형7'
        foodType = 7
    elif request.form['food'] == 'foodType8':
        foodType_str = '맛집유형8'
        foodType = 8


    # 숙소 추가 옵션
    pension_opt_list = ['pet', 'pool', 'garden', 'sea', 'nocost', 'bus']
    for pension_opt in pension_opt_list:
        try:
            request.form[pension_opt]
            globals()[str(pension_opt)] = 1
            globals()[str(pension_opt) +'_str'] = '선택'
        except:
            globals()[str(pension_opt)] = 0
            globals()[str(pension_opt) +'_str'] = '미선택'


    # 주변 추가 옵션
    add_opt_list = ['police', 'hospital', 'bank',  'mart', 'gift']
    for add_opt in add_opt_list:
        try:
            request.form[add_opt]
            globals()[str(add_opt)] = 1
            globals()[str(add_opt) +'_str'] = '선택'
        except:
            globals()[str(add_opt)] = 0
            globals()[str(add_opt) +'_str'] = '미선택'

    # data 추가
    new_data = selectData(month = monthType, month_str = monthType_str,
                          spot1 = spot1Type, spot1_str = spot1Type_str,
                          spot2 = spot2Type, spot2_str = spot2Type_str,
                          food = foodType, food_str = foodType_str,
                          pet = pet, pool = pool, garden = garden, sea = sea, nocost = nocost, bus = bus,
                          police = police, hospital = hospital, bank = bank, mart = mart, gift = gift)
    db.session.add(new_data)
    db.session.commit()

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]

    return render_template("select/select2.html",
                           select_value = select_value)


@bp.route('/select3', methods=('GET', 'POST'))
def show_select3():

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]
    pet_yes = select_value.pet

    fil_con = "TestData.type == 1, pension.ammen.like('%반려동물%'), pension.ammen.like('%대중교통%')"

    if pet_yes == 1:
        type1 = db.session.query(TestData).join(pension, pension.pensionID == TestData.pensionID).filter(TestData.type == 1, pension.ammen.like('%반려동물%'), pension.ammen.like('%대중교통%')).all()
        type2 = db.session.query(TestData).join(pension, pension.pensionID == TestData.pensionID).filter(TestData.type == 2, pension.ammen.like('%반려동물%')).all()
        type3 = db.session.query(TestData).join(pension, pension.pensionID == TestData.pensionID).filter(TestData.type == 3, pension.ammen.like('%반려동물%')).all()
        type4 = db.session.query(TestData).join(pension, pension.pensionID == TestData.pensionID).filter(TestData.type == 4, pension.ammen.like('%반려동물%')).all()

    else:
        type1 = db.session.query(TestData).filter(TestData.type == 1).all()
        type2 = db.session.query(TestData).filter(TestData.type == 2).all()
        type3 = db.session.query(TestData).filter(TestData.type == 3).all()
        type4 = db.session.query(TestData).filter(TestData.type == 4).all()




    test_list = []
    for i in range(len(type1)):
        name = type1[i].pensionID

        hospital = type1[i].cnt_3km
        parm = type2[i].cnt_3km
        mart = type3[i].cnt_5km
        bank = type4[i].cnt_15km

        score = hospital + parm + mart + bank
        test_list.append([name, score, hospital, parm, mart, bank])

    test_df = pd.DataFrame(test_list)
    test_df.columns = ['name', 'score', 'hospital', 'parm', 'mart', 'bank']
    test_df.sort_values(by='score', ascending=False, inplace=True)
    score_list = test_df['score'].sort_values(ascending=False)
    score1, score2, score3 = score_list.head(3).values

    return render_template("select/select3.html",
                           test = test_df, score1 = score1, score2 = score2, score3 = score3)






