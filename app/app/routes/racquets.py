from flask import Flask, request, Response, Blueprint, json
from ..models.racquet import Racquet, RacquetSchema

app_racquets = Blueprint('racquets', __name__)
racquets_schema = RacquetSchema

@app_racquets.route('/api/racquets', methods=['GET'])
def get_all():
    """
    Get All Racquets
    """
    posts = Racquet.get_all()
    data = racquets_schema.dump(posts, many=True)
    return custom_response(data, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )