from flask import Blueprint, jsonify, render_template
from app.utils.database import get_tables

general_bp = Blueprint('general', __name__)

@general_bp.route('/')
def index():
    txt = ''.join(str(i) for i in range(1, 5))
    return render_template('index.html', txt=txt)

@general_bp.route('/tables', methods=['GET'])
def show_tables():
    tables = get_tables()
    return jsonify({'tables': tables})
