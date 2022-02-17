# /semm/semm_app/routes.py

""" Application routes """

from flask import render_template, request, url_for, make_response, redirect, jsonify, make_response
from flask import current_app as app
from functools import wraps

import json

from .verify import verify_credentials

@app.route("/")
def login():
    """ Invite MetaMask (logged in) users to
        sign in with Ethereum """
    return render_template('login.html')

@app.route("/siwe_restricted", methods=["GET", "POST"])
def siwe_restricted():
    """ Validate MetaMask credentials and determine login status """
    if request.method == "POST":
        req = request.get_json() # type: dict
        signature = req['signature'] # type: string
        message = req['message'] # type: string
        print('RECEIVED POSTED METAMASK DATA')
        # res = make_response(jsonify({"message":"MetaMask data received"}), 200)
        credentials_verified = verify_credentials(message, signature)
        if credentials_verified == True:
            return redirect(url_for('siwe_restricted'))
        else:
            return redirect(url_for('credentials_not_verified'))
    else:
        # TODO prevent unauthorized access: refactor with @login_required, sessions, etc.;
        return render_template('siwe_restricted.html')

@app.route('/credentials_not_verified')
def credentials_not_verified():
    return render_template('credentials_not_verified.html')

@app.route("/info")
def info():
    return render_template('info.html')