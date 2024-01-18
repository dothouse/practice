import pandas as pd
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju import db

from jeju.models import TestData
from jeju.models import Sum2

bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/select1')
def open_select1():
    return render_template('select/select1.html')


@bp.route('/select2', methods=('GET', 'POST'))
def show_select2():
    result = request.form

    ### select
    petType = request.form['pet']
    tourType = request.form['info']
    spot1Type = request.form['spot1']
    spot2Type = request.form['spot2']

    ### checkbox
    # 추가 옵션
    
    # pet
    try:
        pet = request.form['add_pet']
        pet = 1
        pet_str = '동반'
    except:
        pet_str = '미동반'


    # gift
    try:
        gift = request.form['add_gift']
        gift = 1
        gift_str = '중요'
    except:
        gift_str = '그닥'

    # police
    try:
        police = request.form['add_police']
        police = 1
        police_str = '중요'
    except:
        police_str = '그닥'

    # bus
    try:
        bus = request.form['add_bus']
        bus = 1
        bus_str = '중요'
    except:
        bus_str = '그닥'

    type1 = db.session.query(TestData).filter(TestData.type == 1).all()
    type2 = db.session.query(TestData).filter(TestData.type == 2).all()
    type3 = db.session.query(TestData).filter(TestData.type == 3).all()
    type4 = db.session.query(TestData).filter(TestData.type == 4).all()

    hospital_km = 10

    test_list = []
    for i in range(len(type1)):
        name = type1[i].name

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


    return render_template("select/select2.html",
                           result=result, petType=petType, tourType=tourType, spot1Type=spot1Type, spot2Type=spot2Type,
                           pet_str=pet_str, gift_str =gift_str, police_str=police_str, bus_str = bus_str,
                           test = test_df, score1 = score1, score2 = score2, score3 = score3)


@bp.route('/select3', methods=('GET', 'POST'))
def show_select3():

    ### select
    petType = request.form['pet']
    # pension_list = Sum2.query.order_by(Sum2.score.desc())


    return render_template("select/select3.html")


