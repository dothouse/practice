
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/')
def slist():
    return render_template('select/select_main.html')