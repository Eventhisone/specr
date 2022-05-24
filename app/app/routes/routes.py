from flask import Flask, request, Response, Blueprint, json

app_routes = Blueprint('routes', __name__)

@app_routes.route('/index', methods=['GET'])
def index():
    return {"greeting":"Welcome to specr"}

@app_routes.route('/api/time', methods=['GET'])
def get_current_time():
    return {'time': time.time()}

@app_routes.route('/api/hello', methods=['GET'])
def hello():
    return {'greeting': 'hola!'}