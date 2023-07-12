from flask import Blueprint, make_response, jsonify

test = Blueprint('test', __name__)


@test.route('/')
def index():
    return make_response(
        jsonify({
            'message': 'test'
        }),
        200
    )

@test.route('/hello')
def hello():
    return make_response(
        jsonify({
            'message': 'hello'
        }),
        200
    )