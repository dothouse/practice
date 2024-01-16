from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect


bp = Blueprint('result', __name__, url_prefix='/result')

@bp.route('', methods=('GET', 'POST'))
def show_result():
    result = request.form
    petType = request.form['pet']
    tourType = request.form['tour']

    return render_template("result/result.html",
                           result=result, petType = petType, tourType= tourType)