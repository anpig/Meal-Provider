from flask import Blueprint
from controller.root import login, ping
from controller.main import get_restaurant_info

bp_root = Blueprint('bp_root', __name__)
bp_main = Blueprint('bp_main', __name__)

bp_root.route('/login', methods=['POST'])(login)
bp_root.route('/ping', methods=['GET'])(ping)

bp_main.route('/restaurant/<id>', methods=['GET'])(get_restaurant_info)

