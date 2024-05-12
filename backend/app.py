from flask import Flask, jsonify, request, abort
from models import db, Staff_Info, Dish_Info, Restaurant_Info, Order_Dish, Orders
import pymysql
import dotenv
import os

dotenv.load_dotenv()
app = Flask(__name__)

db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_host = os.getenv("MYSQL_HOST")
db_port = os.getenv("MYSQL_PORT")
db_name = os.getenv("MYSQL_DATABASE")

app.json.sort_keys = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource Not found'}), 404

@app.route('/login', methods=['POST'])
def login():
    account = request.get_json().get("user_account")
    password = request.get_json().get("user_password")
    staff = Staff_Info.query.filter_by(Gmail=account, Password=password).first()
    if staff is None:
        return jsonify({'outh_token': "", 'user_identity': "invalid_user"})
    return jsonify({'outh_token': "", 'user_identity': staff.Position})

@app.route('/restaurant/<id>', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)