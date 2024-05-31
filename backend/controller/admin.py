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
def add_dish():
    if not check_permission('admin'):
        return jsonify({'error': 'Permission Denied'}), 403
    restaurant_id = request.get_json().get('restaurant_id')
    dish_name = request.get_json().get('name')
    description = request.get_json().get('description')
    combo = request.get_json().get('combo')
    price = request.get_json().get('price')
    filename = request.get_json().get('picture_filename')

    # TODO: check if the file has been uploaded
    picture_exist = True
    path = os.path.join('static', 'dish', filename)
    picture_exist = os.path.isfile(path)
    if not picture_exist:
        return jsonify({'status': "fail", 'error': 'Picture has not been uploaded'})

    new_dish = Dish_Info(
        Name = dish_name, Description = description, 
        Price = price, Picture = filename, 
        RestaurantID = restaurant_id, Combo = combo, 
        Available = True, Rating = 0, 
        RatingCnt = 0, TimesOfOrder = 0
    )
    db.session.add(new_dish)
    db.session.commit()
    return jsonify({'status': 'success'})
    
@jwt_required()
def upload_picture(type):
    if not check_permission('admin'):
        return jsonify({'error': 'Permission Denied'}), 403
    
    restaurant_id = request.form.get('restaurant_id')

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
        restaurant = Restaurant_Info.query.filter_by(RestaurantID=restaurant_id).first()
        restaurant.Cover = filename
        db.session.commit()
    
    return jsonify({'status': 'success', 'filename': filename})

@jwt_required()
def update_menu():
    if not check_permission('admin'):
        return jsonify({'error': 'Permission Denied'}), 403
    
    dishes = request.get_json().get('available_dish_id')
    dishes.sort()
    head = 0
    
    dish_info = Dish_Info.query.order_by(Dish_Info.DishID).all()
    if dish_info[-1].DishID < dishes[-1]:
        return jsonify({'status': 'fail', 'error': f'Invalid dish id {dishes[-1]} or below'})
    for dish in dish_info:
        if dish.DishID == dishes[head]:
            dish.Available = True
            if head != len(dishes) - 1:
                head += 1
        elif dish.DishID > dishes[head] and head != len(dishes) - 1:
            return jsonify({'status': 'fail', 'error': f'Invalid dish id {dishes[head]}'})
        else:
            dish.Available = False
    db.session.commit()
    return jsonify({'status': 'success'})

@jwt_required()
def get_menus():
    if not check_permission('admin'):
        return jsonify({'error': 'Permission Denied'}), 403
    
    returned_data = []
    restaurants = Restaurant_Info.query.all()
    for restaurant in restaurants:
        restaurant_id = restaurant.RestaurantID
        dishes = Dish_Info.query.filter_by(RestaurantID=restaurant_id).all()
        dish_list = []
        for dish in dishes:
            dish_list.append({
                'dish_id': dish.DishID,
                'dish_name': dish.Name,
                'combo': dish.Combo,
                'price': dish.Price,
                'available': dish.Available,
                'ordered_times': dish.TimesOfOrder,
                'rating': dish.Rating
            })
        returned_data.append({
            'restaurant_id': restaurant_id,
            'restaurant_name': restaurant.RestaurantName,
            "phone": restaurant.PhoneNumber,
            "open_time": str(restaurant.OpenTime)[:-3],
            "close_time": str(restaurant.CloseTime)[:-3],
            "overall_rating": restaurant.Rating,
            'dishes': dish_list
        })
    return jsonify({'restaurants': returned_data})

@jwt_required()
def update_price():
    if not check_permission('admin'):
        return jsonify({'error': 'Permission Denied'}), 403
    dish_id = request.get_json().get('dish_id')
    price = request.get_json().get('updated_price')
    print(dish_id, price)
    dish = Dish_Info.query.filter_by(DishID=dish_id).first()
    dish.Price = price
    db.session.commit()
    return jsonify({'status': 'success'})