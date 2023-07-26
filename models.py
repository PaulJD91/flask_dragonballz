from app import db

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    race = db.Column(db.String(64))
    alignment = db.Column(db.String(64))
    special_move = db.Column(db.String(64))
    power_level = db.Column(db.Integer)
    stage_id = db.Column(db.Integer, db.ForeignKey('stages.id'))

class Stage(db.Model):
    __tablename__ = "stages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    terrain = db.Column(db.String(64))
    weather = db.Column(db.String(64))
    

