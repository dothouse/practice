
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('pension', __name__, url_prefix='/pension')

@bp.route('/list')
def plist():
    return render_template('./pension/pension_list.html')

