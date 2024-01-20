
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju import db

from jeju.models import Pension


bp = Blueprint('pension', __name__, url_prefix='/select')

@bp.route('/pension', methods=('GET', 'POST'))
def choice_pension():

    pension_name = request.form['pension_name']
    pension_detail = db.session.query(Pension).filter(Pension.pensionID == pension_name).all()

    return render_template('select/pension_info.html',
                            pension_name = pension_name, pension_detail = pension_detail)
