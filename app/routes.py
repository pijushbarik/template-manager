from flask import render_template
from app import app
from app.form import EditorForm

@app.route('/')
@app.route('/index')
def index():
    form = EditorForm()
    return render_template('index.html', form=form)
