from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.form import EditorForm
from app.models import Template
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def indexFile():
    print(request.method)
    form = EditorForm()
    preview = {'data': 'Save or fetch to preview'}
    return render_template('index.html', form=form)

@app.route('/api/template', methods=['POST'])
def api_template_post():
    json_data = request.get_json()
    template = db.session.query(Template).filter_by(name=json_data['filename']).first()
    if template is None:
        t = Template(name=json_data['filename'], data=str.encode(json_data['data']))
        db.session.add(t)
    else:
        template.data = str.encode(json_data['data'])
    try:
        db.session.commit()
        return jsonify(message='Saved successfully')
    except:
        db.session.rollback()
        return jsonify(message='Could not save. Try using another filename'), 500
        
        

@app.route('/api/template/<string:filename>')
def api_template_get(filename):
    template = Template.query.filter_by(name=filename).first()
    if template is None:
        return jsonify()
    return jsonify(filename=template.name, data=bytes.decode(template.data))

