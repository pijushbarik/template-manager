from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from app.models import Template

class EditorForm(FlaskForm):
    filename = StringField('Company Name', validators=[DataRequired()])
    template_type = RadioField('', choices=[('success', 'Success'), ('failure', 'Failure')])
    template_data = TextAreaField(render_kw={'rows': 15})
    submit_fetch = SubmitField('Fetch')
    submit_save = SubmitField('Save')
    
    def validate_filename(self, filename):
        pass
