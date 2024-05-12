from flask import jsonify, abort
from model.models import Restaurant_Info, Dish_Info

def get_restaurant_info(id):
    restaurant = Restaurant_Info.query.filter_by(RestaurantID=id).first()
    if restaurant is None:
        abort(404)
    returned_data = dict()
    returned_data['id'] = restaurant.RestaurantID
    returned_data['restaurant'] = restaurant.RestaurantName
    returned_data['phone'] = restaurant.PhoneNumber
    returned_data['picture'] = '/static/restaurant/' + restaurant.Picture
    returned_data['description'] = restaurant.Description
    returned_data['rating'] = restaurant.Rating
    returned_data['open_time'] = str(restaurant.OpenTime)
    returned_data['close_time'] = str(restaurant.CloseTime)
    dishes = Dish_Info.query.filter_by(RestaurantID=id, Available=True).all()
    returned_data['meals'] = []
    for dish in dishes:
        dish_data = {}
        dish_data['dish_id'] = dish.DishID
        dish_data['name'] = dish.Name
        dish_data['description'] = dish.Description
        dish_data['price'] = dish.Price
        dish_data['rating'] = dish.Rating
        dish_data['order_times'] = dish.TimesOfOrder
        dish_data['picture'] = '/static/dish/' + dish.Picture 
        returned_data['meals'].append(dish_data)
    return jsonify(returned_data)