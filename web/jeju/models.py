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

class TestData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Float, nullable=False)
    type = db.Column(db.Float, nullable=False)
    cnt_1km = db.Column(db.Float, nullable=False)
    cnt_2km = db.Column(db.Float, nullable=False)
    cnt_3km = db.Column(db.Float, nullable=False)
    cnt_5km = db.Column(db.Float, nullable=False)
    cnt_10km = db.Column(db.Float, nullable=False)
    cnt_15km = db.Column(db.Float, nullable=False)
    cnt_20km = db.Column(db.Float, nullable=False)

class pension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    day = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviewNum = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    pension_keyword = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    ammen = db.Column(db.String(200), nullable=False)
    pensionID = db.Column(db.Float, nullable=False)
    ammen1 = db.Column(db.String(200), nullable=False)
    ammen2 = db.Column(db.String(200), nullable=False)
    ammen3 = db.Column(db.String(200), nullable=False)
    ammen4 = db.Column(db.String(200), nullable=False)
    ammen5 = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)








