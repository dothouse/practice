from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from jeju.models import Test
from jeju.models import Sum2


bp = Blueprint('result', __name__, url_prefix='/result')


@bp.route('', methods=('GET', 'POST'))
def show_result():
    pension_list = Sum2.query.order_by(Sum2.score.desc())
    pension = request.form['finalPension']

    if pension == 'finalPension1':
        pension = pension_list[0]
    elif pension == 'finalPension2':
        pension = pension_list[1]
    elif pension == 'finalPension3':
        pension = pension_list[2]



    return render_template("result/result.html",
                           pension = pension)