
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('office', __name__, url_prefix='/office')

@bp.route('/list')
def olist():
    return render_template('./office/office_list.html')

