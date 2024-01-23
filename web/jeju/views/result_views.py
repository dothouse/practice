import pandas as pd
from flask import Blueprint, render_template, request, url_for, g, flash,  render_template_string
from werkzeug.utils import redirect

import folium

from haversine import haversine

from jeju import db
from jeju.models import selectData, Pension, Hospital, Police, Mart, Bank, Gift, Parm, Tour, Food

bp = Blueprint('result', __name__, url_prefix='/result')


# https://python-visualization.github.io/folium/latest/advanced_guide/flask.html
@bp.route("/", methods=('GET', 'POST'))
def mapping():

    pension_name = request.form['finalPension']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    pension_lat = pension_detail[0].latitude
    pension_lng = pension_detail[0].longitude

    pension_map = folium.Map(location=[pension_lat, pension_lng], zoom_start=14)

    pension_map.get_root().width = "100%"
    pension_map.get_root().height = "600px"
    # 숙소 위치
    # folium.Marker([pension_lat, pension_lng],
    #               tooltip=pension_detail[0].addr,
    #               icon = folium.Icon(icon= 'glyphicon-home', icon_size=(100, 100))).add_to(pension_map)
    folium.Marker([pension_lat, pension_lng],
                  tooltip=pension_detail[0].addr,
                  icon=folium.DivIcon(html=f"""
                              <div><svg>
                                  <circle cx="50" cy="50" r="40" fill="black" opacity="1"/>
                                  <rect x="35", y="35" width="30" height="30", fill="red", opacity="1" 
                              </svg></div>""")).add_to(pension_map)
    # haversine 목표
    goal = (pension_lat, pension_lng)

    select_value = db.session.query(selectData).order_by(selectData.id.desc())[0]
    Tour_selected_str = select_value.spot2_str
    Tour_selected = select_value.spot2

    Food_selected_str = select_value.food_str
    Food_selected = select_value.food


    # 거리 계산하는 함수
    def spot_mapping(category, color, icon, d_type):

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

    if 'tour' in request.form:
        near_tour = spot_mapping(Tour, 'orange', 'glyphicon-heart', Tour_selected)
        tour_selected = 1
    else:
        near_tour = 'none'
        tour_selected = 0

    if 'gift' in request.form:
        near_gift = spot_mapping(Gift, 'green', 'glyphicon-gift', 'none')
        gift_selected = 1
    else:
        near_gift = 'none'
        gift_selected = 0

    if 'food' in request.form:
        near_food = spot_mapping(Food, 'red', 'glyphicon-cutlery',Food_selected)
        food_selected = 1
    else:
        near_food = 'none'
        food_selected = 0



    iframe = pension_map.get_root()._repr_html_()

    return render_template("result/result.html", iframe=iframe,
                           pension_name = pension_name, pension_detail = pension_detail,
                           near_tour = near_tour, tour_selected =tour_selected,
                           near_gift = near_gift, gift_selected =gift_selected,
                           near_food =near_food, food_selected=food_selected,
                           spot2 = Tour_selected, spot2_str = Tour_selected_str,
                           food = Tour_selected, food_str = Food_selected_str)


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