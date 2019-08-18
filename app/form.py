from wtforms import Form, StringField, validators, SubmitField

class EditorForm(Form):
    filename = StringField('Filename', validators=[validators.DataRequired()])
    
