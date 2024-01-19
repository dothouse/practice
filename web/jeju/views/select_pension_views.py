
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju import db

from jeju.models import pension


bp = Blueprint('pension', __name__, url_prefix='/select')

@bp.route('/pension', methods=('GET', 'POST'))
def choice_pension1():

    pension_name = request.form['pension_info']
    pension_detail = db.session.query(pension).filter(pension.pensionID == pension_name).all()

    return render_template('select/pension.html',
                            pension_name = pension_name, pension_detail = pension_detail)
