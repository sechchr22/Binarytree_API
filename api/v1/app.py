#!/usr/bin/python3
'''
Flask app module
'''

from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import make_response, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_session(exception=None):
    '''
    close session method
    '''
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Method to handler a 404 error"""

    return make_response(jsonify({"error": "tree id Not found"}), 404)

if __name__ == '__main__':
    _host = '0.0.0.0'
    _port = '5000'

    app.run(host=_host, port=_port, threaded=True)
