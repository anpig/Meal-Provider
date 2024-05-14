from flask import request, jsonify
from model.models import Dish_Info
from flask_jwt_extended import jwt_required
from controller.user_auth import check_permission, get_restaurant_id

@jwt_required()
def get_menu():
    # obtain from JWT, for now, hard code for testing
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