import pandas as pd
from flask import Blueprint, render_template, request, url_for, session, g, flash

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


from werkzeug.utils import redirect

from sqlalchemy import func

from jeju import db

from jeju.models import TestData, TestTour, pension


bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/select1')
def open_select1():


    return render_template('select/select1.html')


@bp.route('/select2', methods=('GET', 'POST'))
def show_select2():
    # 카테고리 옵션

    # 유형1
    if request.form['month'] == 'monthType1':
        tourType = '유형1'
    elif request.form['month'] == 'monthType2':
        tourType = '유형2'
    elif request.form['month'] == 'monthType3':
        tourType = '유형3'
    elif request.form['month'] == 'monthType4':
        tourType = '유형4'
    elif request.form['month'] == 'monthType5':
        tourType = '유형5'

    # 관광지
    if request.form['spot1'] == 'spot1Type1':
        spot1Type = '관광유형1'
    elif request.form['spot1'] == 'spot1Type2':
        spot1Type = '관광유형2'
    elif request.form['spot1'] == 'spot1Type3':
        spot1Type = '관광유형3'
    elif request.form['spot1'] == 'spot1Type4':
        spot1Type = '관광유형4'
    elif request.form['spot1'] == 'spot1Type5':
        spot1Type = '관광유형5'


    spot2Type = request.form['spot2']

    # 식당
    if request.form['food'] == 'foodType1':
        foodType = '유형1'
    elif request.form['food'] == 'foodType2':
        foodType = '유형2'
    elif request.form['food'] == 'foodType3':
        foodType = '유형3'
    elif request.form['food'] == 'foodType4':
        foodType = '유형4'
    elif request.form['food'] == 'foodType5':
        foodType = '유형5'


    # 숙소 추가 옵션
    try:
        pet = request.form['pet']
        pet = 1
        pet_str = '동반'
    except:
        pet = 0
        pet_str = '미동반'

    try:
        pool = request.form['pool']
        pool = 1
        pool_str = '동반'
    except:
        pool = 0
        pool_str = '미동반'

    try:
        bbq = request.form['bbq']
        bbq = 1
        bbq_str = '동반'
    except:
        bbq = 0
        bbq_str = '미동반'

    try:
        garden = request.form['garden']
        garden = 1
        garden_str = '동반'
    except:
        garden = 0
        garden_str = '미동반'

    try:
        nocost = request.form['nocost']
        nocost = 1
        nocost_str = '동반'
    except:
        nocost = 0
        nocost_str = '미동반'




    # 추가 옵션
    # gift
    try:
        gift = request.form['gift']
        gift = 1
        gift_str = '중요'
    except:
        gift_str = '그닥'

    # police
    try:
        police = request.form['police']
        police = 1
        police_str = '중요'
    except:
        police_str = '그닥'

    # bus
    try:
        bank = request.form['bank']
        bank = 1
        bank_str = '중요'
    except:
        bank_str = '그닥'

    # bank
    try:
        bank = request.form['bank']
        bank = 1
        bank_str = '중요'
    except:
        bank_str = '그닥'

    try:
        parm = request.form['parm']
        parm = 1
        parm_str = '동반'
    except:
        parm = 0
        parm_str = '미동반'

    # data 추가
    new_data = TestTour(tour = tourType, pet = pet)
    db.session.add(new_data)
    db.session.commit()

    return render_template("select/select2.html",
                           tourType=tourType, spot1Type=spot1Type, spot2Type=spot2Type, foodType=foodType,
                           pet_str=pet_str,
                           gift_str=gift_str, police_str=police_str, bank_str=bank_str)


@bp.route('/select3', methods=('GET', 'POST'))
def show_select3():

    select_value = db.session.query(TestTour).order_by(TestTour.id.desc())
    pet_yes = select_value[0].pet

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






