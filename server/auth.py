from flask import flash, jsonify, render_template, request, make_response, Blueprint, redirect, url_for, session
import jwt
import datetime # to expire token
from flask import current_app

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['POST']) # i think its done
def login():
    # dont do this need get by json instead
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.findOneByEmail(email) # sqlalchemy query

    if user is None:
        # send back client error 400
        return make_response('User not found', 400)