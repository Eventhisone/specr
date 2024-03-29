from flask import Flask, request, Response, Blueprint, json
from ..models.racquet import Racquet, RacquetSchema

app_racquets = Blueprint('racquets', __name__)
racquet_schema = RacquetSchema()

@app_racquets.route('/api/racquets', methods=['GET'])
def get_all():
    """
    Get All Racquets
    """
    posts = Racquet.get_all()
    data = racquet_schema.dump(posts, many=True)
    return custom_response(data, 200)

@app_racquets.route('/api/racquets/info', methods=['GET'])
def get_info():
    """
    Get Manufacturer Endpoint Info
    """
    return custom_response({"info": "Racquets endpoint"}, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
