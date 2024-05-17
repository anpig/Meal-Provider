from flask import Blueprint
from controller.root import login, ping
from controller.main import get_restaurant_info
from controller.pos import get_menu, add_dish, upload_picture, get_order, add_order

bp_root = Blueprint('bp_root', __name__)
bp_main = Blueprint('bp_main', __name__)
bp_pos = Blueprint('bp_pos', __name__)

# prefix: /
bp_root.route('/login', methods=['POST'])(login)
bp_root.route('/ping', methods=['GET'])(ping)

# prefix: /main
bp_main.route('/restaurant/<id>', methods=['GET'])(get_restaurant_info)


# prefix: /pos
bp_pos.route('/menu', methods=['GET'])(get_menu)
bp_pos.route('/add_dish', methods=['POST'])(add_dish)
bp_pos.route('/upload/<type>', methods=['POST'])(upload_picture)
bp_pos.route('/get_order', methods=['GET'])(get_order)
bp_pos.route('/add_order', methods=['POST'])(add_order)