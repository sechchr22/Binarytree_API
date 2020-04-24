#!/usr/bin/python3
'''
Flask app INDEX
to make sure our flask app is running
'''

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def status():
    '''
    Get api status
    '''
    return jsonify({'status': 'OK'})
