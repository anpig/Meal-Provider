from flask import request, jsonify
from random import shuffle
from model.models import Dish_Info, db, Restaurant_Info
from flask_jwt_extended import jwt_required
from controller.user_auth import check_permission, get_restaurant_id
import os

UPLOAD_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in UPLOAD_ALLOWED_EXTENSIONS

@jwt_required()
def get_menu():
    if not check_permission('restaurant'):
        return jsonify({'error': 'Permission Denied'}), 403
    restaurant_id = get_restaurant_id()
    dishes = Dish_Info.query.filter_by(RestaurantID=restaurant_id).all()
    menu = []
    for dish in dishes:
        menu.append({
            'dish_id': dish.DishID,
            'name': dish.Name,
            'description': dish.Description,
            'price': dish.Price,
            'rating': dish.Rating,
            "order_times": dish.TimesOfOrder,
            "picture": dish.Picture,
            "available": dish.Available
        })
    return jsonify({'meals': menu})

@jwt_required()
def add_dish():
    if not check_permission('restaurant'):
        return jsonify({'error': 'Permission Denied'}), 403
    restaurant_id = get_restaurant_id()
    dish_name = request.get_json().get('name')
    description = request.get_json().get('description')
    price = request.get_json().get('price')
    filename = request.get_json().get('picture_filename')

    # TODO: check if the file has been uploaded
    picture_exist = True
    path = os.path.join('static', 'dish', filename)
    picture_exist = os.path.isfile(path)
    if not picture_exist:
        return jsonify({'status': "fail", 'error': 'Picture has not been uploaded'})

    new_dish = Dish_Info(
        Name=dish_name, Description=description, 
        Price=price, Picture=filename, 
        RestaurantID=restaurant_id,
        Available=True, Rating=0, TimesOfOrder=0

    )
    db.session.add(new_dish)
    db.session.commit()
    return jsonify({'status': 'success'})
    
@jwt_required()
def upload_picture(type):
    if not check_permission('restaurant'):
        return jsonify({'error': 'Permission Denied'}), 403
   
    # error handling
    if type not in ['cover', 'dish']:
        return jsonify({'status': 'fail', 'error': 'Invalid type'})
    if not allowed_file(request.files['image'].filename):
        return jsonify({'status': 'fail', 'error': 'Invalid file type'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'status': 'fail', 'error': 'No selected file'})

    filename = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    shuffle(filename)
    filename = ''.join(filename[:10]) + '.' + file.filename.split('.')[-1]
    path = os.path.join('static', type, filename)
    file.save(path)

    # TODO test this part
    if type == 'cover':
        restaurant = Restaurant_Info.query.filter_by(RestaurantID=get_restaurant_id()).first()
        restaurant.Cover = filename
        db.session.commit()
    
    return jsonify({'status': 'success', 'filename': filename})