#! /usr/bin/env python
import datetime
import os
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def api_root():
    authHeaders = {'Authorization': 'Basic <Insert Encoded Credentials>'}
    response = requests.get("https://sapes5.sapdevcenter.com/sap/opu/odata/iwbep/GWSAMPLE_BASIC/", headers=authHeaders)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response.content, response.status_code


@app.route('/BusinessPartnerSet', methods=['GET'])
def api_businesspartnerset():
    authHeaders = {'Authorization': 'Basic <Insert Encoded Credentials>'}
    response = requests.get("https://sapes5.sapdevcenter.com/sap/opu/odata/iwbep/GWSAMPLE_BASIC/BusinessPartnerSet?$format=json", headers=authHeaders)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response.content, response.status_code


port = int(os.getenv("PORT", 0))
if __name__ == '__main__':
    if port != 0:
        app.run(host='0.0.0.0', port=port)
    else:
        app.run()
