from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

# @bp.before_app_request
# def select_section():
#     g.month = session.get('tour')


@bp.route('/')
def select1():
    return redirect(url_for('select1.open_select1'))


