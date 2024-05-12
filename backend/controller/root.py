from flask import request, jsonify
from model.models import Staff_Info

def login():
    account = request.get_json().get("user_account")
    password = request.get_json().get("user_password")
    staff = Staff_Info.query.filter_by(Gmail=account, Password=password).first()
    if staff is None:
        return jsonify({'outh_token': "", 'user_identity': "invalid_user"})
    return jsonify({'outh_token': "", 'user_identity': staff.Position})

def ping():
    return jsonify({'message': 'pong'})
