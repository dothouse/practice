from flask import Blueprint, render_template, request, send_file, url_for, g, flash
from werkzeug.utils import redirect

import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

import pandas as pd
from haversine import haversine

import folium

from jeju import db
from jeju.models import selectData, Pension, Hospital, Police, Mart, Bank, Gift, Parm, Tour, Food, Olleh
from jeju.models import Weather, Weather_point, Pm_point, Pm

bp = Blueprint('info', __name__, url_prefix='/info')


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
            if ((category == Tour) & ((d_type % 10) == 1)):
                globals()[str(category) + '_detail'] = db.session.query(category).filter(
                    category.detailtype.like(f'%{d_type}%') | category.detailtype.like(f'%{d_type + 2}%')).all()
            elif ((category == Tour) & ((d_type % 10) == 2)):
                globals()[str(category) + '_detail'] = db.session.query(category).filter(
                    category.detailtype.like(f'%{d_type}%') | category.detailtype.like(f'%{d_type + 1}%')).all()
            else:
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

    return render_template('info/tour_near.html',
                           df_haver=df_haver, df_haver_short=df_haver_short,
                           info_type=info_type,
                           select_type=select_type)


@bp.route('/olleh', methods=('GET', 'POST'))
def olleh():
    pension_name = request.form['finalPension']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    olleh_map = folium.Map(location=[pension_lat, pension_lng], zoom_start=12)

    olleh_map.get_root().width = "100%"
    olleh_map.get_root().height = "600px"
    # 숙소 위치
    # folium.Marker([pension_lat, pension_lng],
    #               tooltip=pension_detail[0].addr,
    #               icon = folium.Icon(icon= 'glyphicon-home', icon_size=(100, 100))).add_to(pension_map)
    folium.Marker([pension_lat, pension_lng],
                  tooltip=pension_detail[0].addr,
                  icon=folium.Icon(icon='glyphicon-home', color='darkblue')).add_to(olleh_map)
    folium.Circle([pension_lat, pension_lng], radius=200,
                  color='red',  # Specify the fill color here
                  fill=True,
                  fill_color='red',  # You can set this to a different color if needed
                  fill_opacity=0.7,
                  ).add_to(olleh_map)

    # haversine 목표
    goal = (pension_lat, pension_lng)

    query_olleh = db.session.query(Olleh).all()

    # mapping
    for i in range(len(query_olleh)):
        folium.Marker(
            location=[query_olleh[i].lat, query_olleh[i].lng],
            tooltip=query_olleh[i].name,
            popup=folium.Popup(query_olleh[i].addr, max_width=200),
            icon=folium.Icon('orange', icon='star')
        ).add_to(olleh_map)

    query_olleh2 = db.session.query(Olleh).filter(
        (Olleh.name != '1-1코스') & (Olleh.name != '7-1코스') & (Olleh.name != '10-1코스')
        & (Olleh.name != '14-1코스') & (Olleh.name != '18-1코스')).all()

    for i in range(len(query_olleh2)):
        if i == (len(query_olleh2) - 1):
            folium.Polygon(locations=[[query_olleh2[i].lat, query_olleh2[i].lng],
                                      [query_olleh2[0].lat, query_olleh2[0].lng]],
                           tooltip=f'{query_olleh2[i].name}').add_to(olleh_map)
        else:
            folium.Polygon(locations=[[query_olleh2[i].lat, query_olleh2[i].lng],
                                      [query_olleh2[i + 1].lat, query_olleh2[i + 1].lng]],
                           tooltip=f'{query_olleh2[i].name}').add_to(olleh_map)

    iframe = olleh_map.get_root()._repr_html_()

    ## 시작점과 숙소와의 거리 계산
    def olleh_haver(df):
        goal = (pension_lat, pension_lng)
        temp_distance = []
        for i in range(len(df)):
            start = (df[i].lat, df[i].lng)
            name = df[i].name
            addr = df[i].addr
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

    df_haver = olleh_haver(query_olleh)
    df_haver_short = select_near(df_haver)

    return render_template('info/olleh.html',
                           iframe=iframe,
                           df_haver=df_haver, df_haver_short=df_haver_short)


@bp.route('/weather', methods=('GET', 'POST'))
def weather():
    pension_name = request.form['finalPension']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    query_wp = db.session.query(Weather_point).all()
    query_pp = db.session.query(Pm_point).all()

    def weather_haver(df):
        goal = (pension_lat, pension_lng)
        temp_distance = []
        for i in range(len(df)):
            start = (df[i].lat, df[i].lng)
            name = df[i].name
            addr = df[i].addr
            haver = haversine(start, goal)
            haver = round(haver, 2)
            temp_distance.append([name, haver, addr])

        temp_distance = pd.DataFrame(temp_distance)
        temp_distance.columns = ['name', 'haver', 'addr']
        return pd.DataFrame(temp_distance)

    def select_near(df):
        temp_distance_list = df['haver'].sort_values(ascending=True)
        near_temp_distance = temp_distance_list.head(1).values[0]
        temp = df[df['haver'] == near_temp_distance]
        return pd.DataFrame(temp)

    wp_haver = weather_haver(query_wp)
    wp_haver_short = select_near(wp_haver)

    pm_haver = weather_haver(query_pp)
    pm_haver_short = select_near(pm_haver)

    wp_spot = wp_haver_short.name.values[0]
    weather_detail = db.session.query(Weather).filter(Weather.point_name == wp_spot).all()

    pp_spot = pm_haver_short.name.values[0]
    pm_detail = db.session.query(Pm.day, Pm.year)

    return render_template('info/weather.html',
                           wp_haver=wp_haver, wp_haver_short=wp_haver_short,
                           pm_haver=pm_haver, pm_haver_short=pm_haver_short,
                           weather_detail=weather_detail, pm_detail=pm_detail)


## 그림을 위한 패키지
from io import BytesIO, StringIO
import base64


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# https://frhyme.github.io/python-lib/flask_matplotlib/
@bp.route('/weather/<point>', methods=('GET', 'POST'))
def weather_fig(point):
    if 'wp_name' in request.form:
        point = request.form['wp_name']
        selected_query = db.session.query(Weather).filter(Weather.point_name == point).all()
    elif 'pm_name' in request.form:
        point = request.form['pm_name']
        selected_query = db.session.query(Pm).filter(Weather.point_name == point).all()
    else:
        point = 'none'
        selected_query = 'none'

    selected_query = db.session.query(Weather).filter(Weather.point_name == point).all()
    temp_list = []
    for i in range(len(selected_query)):
        point_name = selected_query[i].point_name
        date = selected_query[i].date
        temperature = selected_query[i].temperature
        rain = selected_query[i].rain
        temp_list.append({'point_name': point_name,
                          'date': pd.to_datetime(date),
                          'temperature': temperature,
                          'rain': rain})
    df_weather = pd.DataFrame(temp_list)
    df_weather['date'] = pd.to_datetime(df_weather['date'], format='%Y-%M-%d')
    df_weather['date'] = df_weather['date'].dt.strftime('%y-%m-%d')
    df_weather['date'] = pd.to_datetime(df_weather['date'], format='%y-%m-%d')

    plt.figure(figsize=(10, 5))
    plt.title(f"{point} 관측소 정보", fontsize=15)
    plt.plot(df_weather["date"], df_weather["temperature"], "-", color='orange', label=str(point))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=45)
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    img_str = base64.b64encode(img.read()).decode('utf-8')

    return render_template("info/show_weather.html", img_data=img_str)

    # return send_file(img, mimetype='image/png')


@bp.route('/pm/<point>', methods=('GET', 'POST'))
def pm_fig(point):
    if 'pm_name' in request.form:
        point = request.form['pm_name']
        selected_column = getattr(Pm, point)
        selected_query = db.session.query(Pm.date, selected_column).all()
    else:
        point = 'none'
        selected_query = 'none'

    pm_list = []
    for i in range(len(selected_query)):
        date = selected_query[i][0]
        date = pd.to_datetime(date)
        pm = selected_query[i][1]
        pm_list.append({'date': date,
                        'pm': pm})
    df_pm = pd.DataFrame(pm_list)
    df_pm['date'] = pd.to_datetime(df_pm['date'], format='%Y-%M-%d')
    df_pm['date'] = df_pm['date'].dt.strftime('%y-%m-%d')
    df_pm['date'] = pd.to_datetime(df_pm['date'], format='%y-%m-%d')

    df_pm2 = df_pm[df_pm['date'] > '2023-01-01']
    plt.figure(figsize=(10, 5))
    plt.title(f"{point} 관측소 - 미세먼지", fontsize=15)
    plt.plot(df_pm2["date"], df_pm2["pm"], "-", color='orange', label=str(point))
    plt.grid()
    plt.legend(fontsize=13)
    plt.xticks(rotation=45)
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    img_str = base64.b64encode(img.read()).decode('utf-8')

    return render_template("info/show_pm.html", test=df_pm['date'].dtype, img_data=img_str)
