from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def jeju_map():
    return redirect(url_for('select.slist'))

@bp.route('/pension')
def pension():
    return redirect(url_for('pension.plist'))

@bp.route('/tour')
def tour():
    return redirect(url_for('tour.tlist'))

@bp.route('/office')
def office():
    return redirect(url_for('office.olist'))

@bp.route('/restaurant')
def restaurant():
    return redirect(url_for('restaurant.rlist'))

