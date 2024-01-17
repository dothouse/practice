
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju.models import Test, Sum2


bp = Blueprint('pension', __name__, url_prefix='/pension')

@bp.route('/')
def open_pension():
    return render_template('select/pension/pension_list.html')


@bp.route('/pension1')
def choice_pension1():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension1 = pension_list[0]

    return render_template('select/pension/pension1.html',
                           pension1 = pension1)

@bp.route('/pension2')
def choice_pension2():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension2 = pension_list[1]
    return render_template('select/pension/pension2.html',
                           pension2 =pension2)

@bp.route('/pension3')
def choice_pension3():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension3 = pension_list[2]
    return render_template('select/pension/pension3.html',
                           pension3 = pension3)