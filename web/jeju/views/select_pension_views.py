
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju import db

from jeju.models import Test, Sum2, pension


bp = Blueprint('pension', __name__, url_prefix='/select')

@bp.route('/')
def open_pension():
    return render_template('select/pension/pension_list.html')


@bp.route('/pension1', methods=('GET', 'POST'))
def choice_pension1():

    pension_name = request.form['pension_info']
    pension_detail = db.session.query(pension).filter(pension.pensionID == pension_name).all()

    return render_template('select/pension/pension1.html',
                            pension_name = pension_name, pension_detail = pension_detail)

@bp.route('/pension2')
def choice_pension2():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension2 = pension_list[1]
    return render_template('select/pension/pension2.html',
                           pension2 =pension2)

@bp.route('/pension3', methods=('GET', 'POST'))
def choice_pension3():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension3 = pension_list[2]

    pension_name = request.form['value']

    return render_template('select/pension/pension3.html',
                           pension3 = pension3)