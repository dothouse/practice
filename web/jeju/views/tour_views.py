
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('tour', __name__, url_prefix='/tour')

@bp.route('/list')
def tlist():
    return render_template('./tour/tour_list.html')