
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('info', __name__, url_prefix='/info')

@bp.route('/')
def tlist():
    return render_template('info/tour_list.html')

@bp.route('/restaurant')
def open_restaurant():
    return render_template('info/restaurant_list.html')


@bp.route('/tour')
def open_tour():
    return render_template('info/tour_list.html')

@bp.route('/office')
def open_office():
    return render_template('info/office_list.html')

