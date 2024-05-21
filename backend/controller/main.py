from flask import jsonify, abort, request
from model.models import Restaurant_Info, Dish_Info, Review, Orders, Order_Dish, db
from controller.user_auth import check_permission
from flask_jwt_extended import jwt_required
from datetime import datetime

@jwt_required()
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

@jwt_required()
def add_review():
    permission_warning = False
    if check_permission('worker') == False:
        permission_warning = True

    order_id = request.get_json().get('order_id')
    overall_rating = request.get_json().get('overall_rating')
    dishes_rating = request.get_json().get('dishes_rating')
    print(type(dishes_rating))
    
    order = Orders.query.filter_by(OrderID=order_id).first()
    if order is None:
        return jsonify({'error': 'Order not found'}), 404
    if order.Reviewed:
        return jsonify({'error': 'Order has been reviewed'}), 403
    if not order.Finish:
        return jsonify({'error': 'Order not finished'}), 403
    
    reviews = []
    for dish in dishes_rating:
        review = Review(OrderID=order_id, DishID=dish['dish_id'], Rating=dish['rating'], Time=datetime.now(), CustomerID=order.CustomerID)
        check_order = Order_Dish.query.filter_by(OrderID=order_id, DishID=dish['dish_id']).first()
        if check_order is None:
            return jsonify({'error': 'Dish not found in order'}), 404
        reviews.append(review)

        # update dish rating
        dish_info = Dish_Info.query.filter_by(DishID=dish['dish_id']).first()
        dish_info.Rating = (dish_info.Rating * dish_info.RatingCnt + dish['rating']) / (dish_info.RatingCnt + 1)
        dish_info.RatingCnt += 1
    reviews.append(Review(OrderID=order_id, DishID=0, Rating=overall_rating, Time=datetime.now(), CustomerID=order.CustomerID)) # overall rating
    # update restaurant rating
    restaurant_info = Restaurant_Info.query.filter_by(RestaurantID=order.RestaurantID).first()
    restaurant_info.Rating = (restaurant_info.Rating * restaurant_info.RatingCnt + overall_rating) / (restaurant_info.RatingCnt + 1)
    restaurant_info.RatingCnt += 1
    order.Reviewed = True
    db.session.add_all(reviews)
    db.session.commit()
    
    if permission_warning:
        return jsonify({'status': 'success', 'warning': 'You are not using worker permission'})
    return jsonify({'status': 'success'})