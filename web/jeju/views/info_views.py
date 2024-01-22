
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

import pandas as pd
from haversine import haversine

from jeju import db
from jeju.models import selectData, Pension, Hospital, Police, Mart, Bank, Gift, Parm, Tour, Food


bp = Blueprint('info', __name__, url_prefix='/info')

@bp.route('/')
def tlist():
    return render_template('info/tour_info.html')

@bp.route('/restaurant')
def open_restaurant():
    return render_template('info/restaurant_list.html')


@bp.route('/tour', methods=('GET', 'POST'))
def open_tour():
    pension_name = request.form['finalPension']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    # haversine 목표
    goal = (pension_lat, pension_lng)

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]
    Tour_selected_str = select_value.spot2_str
    Tour_selected = select_value.spot2
    Food_selected_str = select_value.food_str
    Food_selected = select_value.food

    def cal_haver(category, d_type):
        goal = (pension_lat, pension_lng)
        if d_type != 'none':
            globals()[str(category) + '_detail'] = db.session.query(category).filter(
                category.detailtype.like(f'%{d_type}%')).all()
        else:
            globals()[str(category) + '_detail'] = db.session.query(category).all()
        temp_distance = []
        temp_detail = globals()[str(category) + '_detail']
        for i in range(len(temp_detail)):
            start = (temp_detail[i].lat, temp_detail[i].lng)
            name = temp_detail[i].name
            addr = temp_detail[i].addr
            haver = haversine(start, goal)
            haver = round(haver, 2)
            temp_distance.append([name, haver, addr])

        temp_distance = pd.DataFrame(temp_distance)
        temp_distance.columns = ['name', 'haver', 'addr']

        return pd.DataFrame(temp_distance)

    def select_near(df):
        temp_haver = df['haver'].sort_values()
        temp_haver_short = temp_haver.head(10).to_list()
        temp = df[df['haver'].isin(temp_haver_short)]

        return pd.DataFrame(temp)


    if request.form['more'] == '관광지 더보기':
        df_haver = cal_haver(Tour, Tour_selected)
        df_haver_short = select_near(df_haver)
        info_type = request.form['more']
        select_type = Tour_selected_str
    elif request.form['more'] == '기념품 더보기':
        df_haver = cal_haver(Gift, 'none')
        df_haver_short = select_near(df_haver)
        info_type = request.form['more']
        select_type = ""
    elif request.form['more'] == '맛집 더보기':
        df_haver = cal_haver(Food, Food_selected)
        df_haver_short = select_near(df_haver)
        info_type = request.form['more']
        select_type = Food_selected_str
    else:
        df_haver = 'none'
        df_haver_short = 'none'
        info_type = 'none'
        select_type = ''





    return render_template('info/tour_info.html',
                           df_haver  = df_haver, df_haver_short = df_haver_short,
                           info_type = info_type,
                           select_type = select_type)


@bp.route('/gift')
def open_gift():
    return render_template('info/gift_list.html')

@bp.route('/office' , methods=('GET', 'POST'))
def open_office():
    return render_template('info/office_list.html')

