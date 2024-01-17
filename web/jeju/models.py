from jeju import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewNum = db.Column(db.Float, nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)

class Sum2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Float, nullable=False)





