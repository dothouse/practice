from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju.models import Test
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
        pet_str = '동반'
    except:
        pet_str = '미동반'


    # gift
    try:
        gift = request.form['add_gift']
        gift_str = '중요'
    except:
        gift_str = '그닥'

    # police
    try:
        police = request.form['add_police']
        police_str = '중요'
    except:
        police_str = '그닥'

    # bus
    try:
        bus = request.form['add_bus']
        bus_str = '중요'
    except:
        bus_str = '그닥'




    pension_list = Sum2.query.order_by(Sum2.score.desc())

    return render_template("select/select2.html",
                           result=result, petType=petType, tourType=tourType,
                           spot1Type=spot1Type, spot2Type=spot2Type,
                           pet_str=pet_str, gift_str =gift_str,
                           police_str=police_str, bus_str = bus_str,
                           pension_list=pension_list)


@bp.route('/select3', methods=('GET', 'POST'))
def show_select3():

    pension_list = Sum2.query.order_by(Sum2.score.desc())

    return render_template("select/select3.html",
                           pension_list = pension_list)


