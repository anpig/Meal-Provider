from flask import request, jsonify
from model.models import Dish_Info

def get_menu():
    # obtain from JWT, for now, hard code for testing
    restaurant_id = 1
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