from flask import Blueprint, jsonify
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/status', methods=['GET'])
@login_required
def status():
    return jsonify({
        'message': 'Game instance is running',
        'user': current_user.email
    })
