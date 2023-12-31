from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return '안녕 파이보, 연습중이야2'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',
                           question_list = question_list)

@bp.route('/test')
def testpage():
    return '연습용 페이지'

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',
                           question = question)


### 2-5 질문 목록, 질문 상세 기능 분리하기