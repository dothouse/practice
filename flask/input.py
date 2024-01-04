from pybo.models import Question, Answer
from datetime import datetime

q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.',
             create_date=datetime.now())

# from pybo import db
# db.session.add(q)
# db.session.commit()

