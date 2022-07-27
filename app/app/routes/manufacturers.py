from flask import Flask, request, Response, Blueprint, json
from ..models.manufacturer import Manufacturer, ManufacturerSchema

app_manufacturers = Blueprint('manufacturers', __name__)
manufacturers_schema = ManufacturerSchema

@app_manufacturers.route('/api/manufacturers', methods=['GET'])
def get_all():
    """
    Get All Manufacturers
    """
    posts = Manufacturer.get_all()
    data = manufacturers_schema.dump(posts, many=True)
    return custom_response(data, 200)

@app_manufacturers.route('/api/manufacturers/info', methods=['GET'])
def get_info():
    """
    Get Manufacturer Endpoint Info
    """
    return custom_response({"info": "Manufacturers endpoint"}, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )