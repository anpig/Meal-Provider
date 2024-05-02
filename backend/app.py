from flask import Flask, jsonify, request
from models import db, Staff_Information
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


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
db.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    account = request.form.get("user_account")
    password = request.form.get("user_password")
    staff = Staff_Information.query.filter_by(Gmail=account, Password=password).first()
    if staff is None:
        return jsonify({'outh_token': "", 'user_identity': "invalid_user"})
    return jsonify({'outh_token': "", 'user_identity': staff.Position})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)