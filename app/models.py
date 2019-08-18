from app import db

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    template_name = db.Column(db.String, index=True, unique=True)
    template_data = db.Column(db.BLOB())
