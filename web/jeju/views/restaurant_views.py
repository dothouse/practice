
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('restaurant', __name__, url_prefix='/restaurant')

@bp.route('/list')
def rlist():
    return render_template('./restaurant/restaurant_list.html')

