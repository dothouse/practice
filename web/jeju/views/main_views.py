from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju.models import Test

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def select1():
    return redirect(url_for('select.open_select1'))

# @bp.route('/pension')
# def pension():
#     return redirect(url_for('pension.open_pension'))

# @bp.route('/info')
# def tour():
#     return redirect(url_for('info.tlist'))
#
# @bp.route('/office')
# def office():
#     return redirect(url_for('office.open_office'))
#
# @bp.route('/restaurant')
# def restaurant():
#     return redirect(url_for('restaurant.open_restaurant'))
