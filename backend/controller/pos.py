from flask import request, jsonify
from model.models import Dish_Info, db
from flask_jwt_extended import jwt_required
from controller.user_auth import check_permission, get_restaurant_id

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
    filename = request.get_json().get('picture')

    # TODO: check if the file has been uploaded
    picture_exist = True
    if not picture_exist:
        return jsonify({'error': 'Picture has not been uploaded'})

    new_dish = Dish_Info(
        Name=dish_name, Description=description, 
        Price=price, Picture=filename, 
        RestaurantID=restaurant_id,
        Available=True, Rating=0, TimesOfOrder=0

    )
    db.session.add(new_dish)
    db.session.commit()
    return jsonify({'status': 'success'})
    