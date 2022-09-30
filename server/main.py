from flask import Flask, jsonify, request, make_response
import shelve
import os

# start flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_secret')

# TODO: configure/initialise db with all "tables"

# configure routes
with app.app_context():
    from auth import auth
    # from api import api
    
app.register_blueprint(auth, url_prefix='/auth')

@app.route("/api/test", methods=['GET'])
def test():
    return jsonify({'message': 'hEllo yES woRking :")'})
    
# app.register_blueprint(api, url_prefix='/api')

# configure warnings
if os.environ.get('JWT_secret') is None:
    print('->> JWT_secret not set in environment!!')
if os.environ.get('FLASK_secret') is None:
    print('->> FLASK_secret not set in environment!!')

print('hereee', os.environ.get('JWT_secret'))

# UPLOAD_FOLDER = 'static/assets/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)
