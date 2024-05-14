from flask import request, jsonify
from model.models import Staff_Info

def login():
    account = request.get_json().get("user_account")
    password = request.get_json().get("user_password")
    staff = Staff_Info.query.filter_by(Gmail=account, Password=password).first()
    if staff is None:
        return jsonify({'outh_token': "", 'user_identity': "invalid_user"})
    if staff.Position.find("restaurant") == -1:
        return jsonify({'outh_token': "", 'user_identity': staff.Position})
    else:
        return jsonify({'outh_token': "", 'user_identity': "restaurant", 'restaurant_id': staff.Position.split('_')[1]})

def ping():
    return jsonify({'message': 'pong'})
