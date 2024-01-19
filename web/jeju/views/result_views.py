import pandas as pd
from flask import Blueprint, render_template, request, url_for, g, flash,  render_template_string
from werkzeug.utils import redirect

import folium

from haversine import haversine

from jeju import db
from jeju.models import TestData, TestTour, pension, Hospital, Police, Mart, Bank, Gift, Parm

bp = Blueprint('result', __name__, url_prefix='/result')


# https://python-visualization.github.io/folium/latest/advanced_guide/flask.html
@bp.route("/", methods=('GET', 'POST'))
def mapping():

    pension_name = request.form['finalPension']
    pension_detail = db.session.query(pension).filter(pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    pension_map = folium.Map(location=[pension_lat, pension_lng], zoom_start=14)

    pension_map.get_root().width = "800px"
    pension_map.get_root().height = "600px"

    # 숙소 위치
    folium.Marker([pension_lat, pension_lng],
                  tooltip=pension_detail[0].addr,
                  icon = folium.Icon(icon= 'glyphicon-home')).add_to(pension_map)
    # haversine 목표
    goal = (pension_lat, pension_lng)


    # 일요일 병원
    hospital_detail = db.session.query(Hospital).all()
    hospital_sun_distance = []
    for i in range(len(hospital_detail)):
        if hospital_detail[i].sun == 1:
            start = (hospital_detail[i].lat, hospital_detail[i].lng)
            name = hospital_detail[i].name
            addr = hospital_detail[i].addr
            sun = hospital_detail[i].sun
            haver = haversine(start, goal)
            haver = round(haver, 2)
            hospital_sun_distance.append([name, haver, addr, sun])
    hospital_sun_distance = pd.DataFrame(hospital_sun_distance)
    hospital_sun_distance.columns = ['name', 'haver', 'addr', 'sun']
    hospital_sun_distance_list = hospital_sun_distance['haver'].sort_values(ascending=True)

    near_hospital_sun_distance = hospital_sun_distance_list.head(1).values[0]
    near_hospital_sun = hospital_sun_distance[hospital_sun_distance['haver'] == near_hospital_sun_distance]



    # 거리 계산하는 함수
    def category_mapping(category, color, icon):
        goal = (pension_lat, pension_lng)
        globals()[str(category)+ '_detail'] = db.session.query(category).all()
        temp_distance = []
        temp_detail = globals()[str(category) + '_detail']
        for i in range(len(temp_detail)):
            start = (temp_detail[i].lat, temp_detail[i].lng)
            name = temp_detail[i].name
            addr = temp_detail[i].addr
            haver = haversine(start, goal)
            haver = round(haver, 2)
            temp_distance.append([name, haver, addr])

            # mapping
            if haver < 10:
                folium.Marker(
                    location=[temp_detail[i].lat, temp_detail[i].lng],
                    tooltip=temp_detail[i].name,  # 마커에 마우스를 올렸을 때 표시되는 툴팁으로 병원명 표시
                    popup=folium.Popup(temp_detail[i].addr, max_width=200),
                    icon=folium.Icon(color=color, icon=icon)
                ).add_to(pension_map)

        temp_distance = pd.DataFrame(temp_distance)
        temp_distance.columns = ['name', 'haver', 'addr']
        temp_distance_list = temp_distance['haver'].sort_values(ascending=True)
        near_temp_distance = temp_distance_list.head(1).values[0]

        return  temp_distance[temp_distance['haver'] == near_temp_distance]

    near_hospital = category_mapping(Hospital, 'yellow', 'glyphicon-map-marker')
    near_police = category_mapping(Police, 'blue', 'glyphicon-map-marker')
    near_mart = category_mapping(Mart, 'purple', 'glyphicon-shopping-cart')
    near_bank = category_mapping(Bank, 'red', 'glyphicon-usd')
    near_parm = category_mapping(Parm, 'green', 'glyphicon-plus')


    iframe = pension_map.get_root()._repr_html_()

    return render_template("result/result.html", iframe=iframe,
                           pension_name = pension_name, pension_detail = pension_detail,
                           near_hospital = near_hospital, near_hospital_sun = near_hospital_sun,
                           near_police = near_police, near_mart = near_mart, near_bank = near_bank,
                           near_parm= near_parm)


@bp.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map()

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


@bp.route("/components")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        width=800,
        height=600,
    )

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                    {{ header|safe }}
                </head>
                <body>
                    <h1>Using components</h1>
                    {{ body_html|safe }}
                    <script>
                        {{ script|safe }}
                    </script>
                </body>
            </html>
        """,
        header=header,
        body_html=body_html,
        script=script,
    )