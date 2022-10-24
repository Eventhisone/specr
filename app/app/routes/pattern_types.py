from flask import Flask, request, Response, Blueprint, json
from ..models.pattern_type import PatternType, PatternTypeSchema

app_pattern_types = Blueprint('pattern_types', __name__)
pattern_types_schema = PatternTypeSchema

@app_pattern_types.route('/api/pattern_types', methods=['GET'])
def get_all():
    """
    Get All Pattern_Types
    """
    posts = PatternType.get_all()
    data = pattern_types_schema.dump(posts, many=True)
    return custom_response(data, 200)

@app_pattern_types.route('/api/pattern-types/info', methods=['GET'])
def get_info():
    """
    Get Manufacturer Endpoint Info
    """
    return custom_response({"info": "PatternType endpoint"}, 200)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )