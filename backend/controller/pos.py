from flask import request, jsonify
from random import shuffle
from model.models import Dish_Info, db, Restaurant_Info, Orders, Staff_Info, Order_Dish
from flask_jwt_extended import jwt_required
from controller.user_auth import check_permission, get_restaurant_id
import os
from datetime import datetime

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

@jwt_required()
def get_order():
    if not check_permission('restaurant'):
        return jsonify({'error': 'Permission Denied'}), 403
    restaurant_id = get_restaurant_id()
    today = datetime(year=datetime.now().year, month=datetime.now().month, day=1)
    orders = db.session.query(Orders, Staff_Info) \
        .join(Staff_Info, Orders.CustomerID == Staff_Info.StaffID, isouter=True) \
        .filter(Orders.RestaurantID == restaurant_id) \
        .filter(Orders.OrderTime >= today) \
        .filter(Orders.OrderTime <= datetime.now()).all()
    order_list = []
    for order in orders:
        order_id = order[0].OrderID
        dishes = db.session.query(Order_Dish, Dish_Info) \
            .join(Dish_Info, Order_Dish.DishID == Dish_Info.DishID, isouter=True) \
            .filter(Order_Dish.OrderID == order_id).all()
        dish_list = [{"dish_id": dish[0].OrderID, "dish_name": dish[1].Name} for dish in dishes]
        # order is a tuple of (Orders, Staff_Info)
        order_list.append({
            'order_id': order[0].OrderID,
            'customer_id': order[0].CustomerID,
            'customer_name': order[1].StaffName,  # Update the column name to Staff_Info.StaffName
            'price': order[0].TotalPrice,
            'order_time': order[0].OrderTime,
            'finish': order[0].Finish,
            'dishes': dish_list
        })
    return jsonify({'orders': order_list})

@jwt_required()
def add_order():
    if not check_permission('restaurant'):
        return jsonify({'error': 'Permission Denied'}), 403
    restaurant_id = get_restaurant_id()
    customer_id = request.get_json().get('customer_id')
    dish_list = request.get_json().get('dishes_id')
    total_price = request.get_json().get('total_price')
    new_order = Orders(
        CustomerID = customer_id, RestaurantID = restaurant_id,
        TotalPrice = total_price, OrderTime = datetime.now(),
        Finish = False
    )
    db.session.add(new_order)
    db.session.commit()
    order_id = new_order.OrderID

    dishes = [Order_Dish(OrderID = order_id, DishID = dish_id) for dish_id in dish_list]
    db.session.add_all(dishes)
    db.session.commit()

    return jsonify({'status': 'success', "order_id": order_id})