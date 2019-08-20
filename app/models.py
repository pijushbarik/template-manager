from app import db

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    data = db.Column(db.BLOB())
