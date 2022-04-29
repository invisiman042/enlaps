import os, sys
# sys.path.insert(1, r'C:\Users\33638\OneDrive\Bureau\PYTHON\enlaps')
sys.path.insert(1, r'C:\Users\nicol\Desktop\enlaps_python\enlaps')
from flask import Flask, render_template, request, url_for
from graphql_requests.main import get_query_response

# create and configure the app
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/tikoo')
def tikoo():
    return render_template('input_form.html')

@app.route('/tikoo', methods=['POST'])
def tikoo_query():
    response = get_query_response('tikee_query', {"id": int(request.form['text'])})
    return render_template('tikee_info_display.html', results=response['tikee'])

@app.route('/tikoo_sn')
def tikoo_sn():
    return render_template('sn_input_form.html')

@app.route('/tikoo_sn', methods=['POST'])
def tikee_by_sn_query():
    response = get_query_response('tikee_by_sn', {"search": [{"field": "serial_number", "value": str(request.form['text'])}], "globalFetch": True})
    return render_template('tikee_sn_info_display.html', results=response['tikees']['nodes'][0])
    # return response