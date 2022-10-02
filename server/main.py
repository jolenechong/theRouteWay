from flask import Flask, jsonify, request, make_response, json
import shelve
import os
import datetime
from functools import total_ordering
from math import floor

# start flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_secret')

from flask_cors import CORS
CORS(app, support_credentials=True)

# configure routes
with app.app_context():
    from auth import auth
    from api import api
    
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(api, url_prefix='/api')
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)
