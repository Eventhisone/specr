from flask import Blueprint


app_routes = Blueprint('routes', __name__)

@app_routes.route('/index', methods=['GET'])
def index():
    return {
        "greeting":"Welcome to specr"
        }
