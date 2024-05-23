from flask import Blueprint
from controller.root import login, ping
from controller.main import get_restaurant_info, add_review, history
from controller.pos import get_menu, get_order, add_order, finish_order
from controller.admin import add_dish, upload_picture

bp_root = Blueprint('bp_root', __name__)
bp_main = Blueprint('bp_main', __name__)
bp_pos = Blueprint('bp_pos', __name__)
bp_admin = Blueprint('bp_admin', __name__)

# prefix: /
bp_root.route('/login', methods=['POST'])(login)
bp_root.route('/ping', methods=['GET'])(ping)

# prefix: /main
bp_main.route('/restaurant/<id>', methods=['GET'])(get_restaurant_info)
bp_main.route('/add_review', methods=['POST'])(add_review)
bp_main.route('/history', methods=['GET'])(history)

# prefix: /pos
bp_pos.route('/menu', methods=['GET'])(get_menu)
bp_pos.route('/get_order', methods=['GET'])(get_order)
bp_pos.route('/add_order', methods=['POST'])(add_order)
bp_pos.route('/finish/<order_id>', methods=['POST'])(finish_order)

# prefix: /admin
bp_admin.route('/add_dish', methods=['POST'])(add_dish)
bp_admin.route('/upload/<type>', methods=['POST'])(upload_picture)
