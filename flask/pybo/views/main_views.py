from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return '안녕 파이보, 연습중이야2'

@bp.route('/')
def index():
    return '메인페이지 - 인덱스'

@bp.route('/test')
def testpage():
    return '연습용 페이지'