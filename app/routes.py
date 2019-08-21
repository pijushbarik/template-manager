from flask import render_template, flash, request, redirect, url_for, jsonify
from app import app, db
from app.form import EditorForm
from app.models import Company, TemplateSuccess, TemplateFailure
from sqlalchemy import exc
import sys

@app.route('/')
def indexFile():
    form = EditorForm()
    return render_template('index.html', form=form)

@app.route('/api/template', methods=['POST'])
def api_template_post():
    json_data = request.get_json()
    # search for company
    c = Company.query.filter_by(name=json_data['company']).first()
    if c is None:
        # does not exist
        # create a new one
        c = Company(name=json_data['company'])
        db.session.add(c)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(message='Unable to save data'), 500
        # finally again set the value of c to the result of search query
        # for later reference
        c = Company.query.filter_by(name=json_data['company']).first()
    
    # set/update template data
    if json_data['ttype'] == 'success':
        # template type = success
        # search for template
        ts = db.session.query(TemplateSuccess).filter_by(company=c).first()
        if ts is None:
            # template does not exist
            # create new one
            ts = TemplateSuccess(company=c, data=str.encode(json_data['data']))
            db.session.add(ts)
        else:
            # template does exist
            # update data
            ts.data = str.encode(json_data['data'])
    elif json_data['ttype'] == 'failure':
        # template type = failure
        # search for template
        tf = db.session.query(TemplateSuccess).filter_by(company=c).first()
        if tf is None:
            # template does not exist
            # create new one
            tf = TemplateFailure(company=c, data=str.encode(json_data['data']))
            db.session.add(tf)
        else:
            # template does exist
            # update data
            tf.data = str.encode(json_data['data'])
    
    # commit
    try:
        db.session.commit()
    except exc.SQLAlchemyError as err:
        print(err)
        db.session.rollback()
        return jsonify(message='Unable to save data'), 500

    return jsonify(message='Saved successfully')

@app.route('/api/template/<string:company>/<string:ttype>')
def api_template_get(company, ttype):
    # search for company
    c = Company.query.filter_by(name=company).first()
    if c is not None:
        # exist
        if ttype == 'success':
            # template type requested is success
            # find template
            t = TemplateSuccess.query.filter_by(company=c).first()
            if t is not None:
                # template found. return data
                return jsonify(data=bytes.decode(t.data))
        elif ttype == 'failure':
            # template type requested is failure
            # find template
            t = TemplateFailure.query.filter_by(company=c).first()
            if t is not None:
                # template found. return data
                return jsonify(data=bytes.decode(t.data))

    # template not found
    return jsonify()
