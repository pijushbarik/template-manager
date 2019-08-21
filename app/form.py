from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, InputRequired

class EditorForm(FlaskForm):
    company = StringField('Company Name', validators=[DataRequired()])
    template_type = RadioField('', choices=[('success', 'Success'), ('failure', 'Failure')],\
        default='success')
    template_data = TextAreaField(render_kw={'rows': 15})
    submit_fetch = SubmitField('Fetch')
    submit_save = SubmitField('Save')
