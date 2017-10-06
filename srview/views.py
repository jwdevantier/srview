from flask import Flask, send_from_directory, render_template
import requests as rq
from requests.compat import urljoin
import json
import srview.utils.avsc as uavsc
from srview import app, logger


SCHEMA_REG_URL = '127.0.0.1:8081'

def endpoint(path):
    return urljoin("http://{0}".format(SCHEMA_REG_URL), path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/<path:path>')
def get_asset(path):
    return send_from_directory('assets', path)

@app.route('/subjects')
def schemas_index():
    subjects = rq.get(endpoint("/subjects")).json()
    logger.info(endpoint("/subjects"))
    logger.info(subjects)
    return render_template('subjects.html', subjects=subjects)

def reencode_schema(schema_str):
    try:
        return json.loads(schema_str)
    except json.decoder.JSONDecodeError:
        return schema_str

@app.route('/subjects/<string:subject>')
def subject_get(subject):
    subject = rq.get(endpoint("/subjects/{0}/versions/latest".format(subject))).json()
    subject['schema'] = reencode_schema(subject['schema'])
    #fun = json.dumps(subject['schema']['fields'], indent=2, sort_keys=True)
    logger.error(subject)
    logger.error("HS")
    
    ctx = {
        'subject': subject,
        'schematype': uavsc.schema_type(subject['schema']),
        'getname': uavsc.schema_name
    }
    logger.error(ctx)
    return render_template(
        'subject.html', 
        **ctx)