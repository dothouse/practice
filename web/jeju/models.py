from jeju import db

class selectData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.INT, nullable=False)
    month_str= db.Column(db.String(200), nullable=False)
    spot1 = db.Column(db.INT, nullable=False)
    spot1_str= db.Column(db.String(200), nullable=False)
    spot2 = db.Column(db.INT, nullable=False)
    spot2_str= db.Column(db.String(200), nullable=False)
    food = db.Column(db.INT, nullable=False)
    food_str= db.Column(db.String(200), nullable=False)
    pet = db.Column(db.INT, nullable=False)
    pet_str = db.Column(db.String(200), nullable=False)
    pool = db.Column(db.INT, nullable=False)
    garden = db.Column(db.INT, nullable=False)
    sea = db.Column(db.INT, nullable=False)
    nocost = db.Column(db.INT, nullable=False)
    bus = db.Column(db.INT, nullable=False)
    police = db.Column(db.INT, nullable=False)
    hospital = db.Column(db.INT, nullable=False)
    bank = db.Column(db.INT, nullable=False)
    mart = db.Column(db.INT, nullable=False)
    gift = db.Column(db.INT, nullable=False)


class TestData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pensionID = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Float, nullable=False)
    cnt_1km = db.Column(db.Float, nullable=False)
    cnt_2km = db.Column(db.Float, nullable=False)
    cnt_3km = db.Column(db.Float, nullable=False)
    cnt_5km = db.Column(db.Float, nullable=False)
    cnt_10km = db.Column(db.Float, nullable=False)
    cnt_15km = db.Column(db.Float, nullable=False)
    cnt_20km = db.Column(db.Float, nullable=False)


class Pension(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviewNum = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    pension_keyword = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    ammen = db.Column(db.String(200), nullable=False)
    pensionID = db.Column(db.Integer, nullable=False)
    ammen1 = db.Column(db.String(200), nullable=False)
    ammen2 = db.Column(db.String(200), nullable=False)
    ammen3 = db.Column(db.String(200), nullable=False)
    ammen4 = db.Column(db.String(200), nullable=False)
    ammen5 = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    sat = db.Column(db.Integer, nullable=False)
    sun = db.Column(db.Integer, nullable=False)
    holiday = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)

class Police(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    homepage = db.Column(db.String(200), nullable=False)

class Parm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Mart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    addr = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    dong = db.Column(db.String(200), nullable=False)
    review_rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(200), nullable=False)
    homepage = db.Column(db.String(200), nullable=False)










