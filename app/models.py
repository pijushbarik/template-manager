from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    template_success = db.relationship('TemplateSuccess', backref='company', lazy='dynamic')
    template_failure = db.relationship('TemplateFailure', backref='company', lazy='dynamic')

class TemplateSuccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), db.ForeignKey('company.name'))
    data = db.Column(db.BLOB())

class TemplateFailure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), db.ForeignKey('company.name'))
    data = db.Column(db.BLOB())
