from flask import request, jsonify
from model.models import Staff_Info
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def login():
    account = request.get_json().get("user_account")
    password = request.get_json().get("user_password")
    staff = Staff_Info.query.filter_by(Gmail=account, Password=password).first()
    if staff is None:
        return jsonify({'outh_token': "", 'user_identity': "invalid_user"})
    access_token = create_access_token(identity=staff.StaffID, additional_claims={'position': staff.Position})
    if staff.Position.find("restaurant") == -1:
        return jsonify({'outh_token': access_token, 'user_identity': staff.Position})
    else:
        return jsonify({'outh_token': access_token, 'user_identity': "restaurant", 'restaurant_id': staff.Position.split('_')[1]})

def ping():
    return jsonify({'message': 'pong'})
