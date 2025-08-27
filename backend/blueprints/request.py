from flask import Blueprint, request, jsonify
import random
from datetime import datetime, timedelta
import string

request_bp = Blueprint('request', __name__)

SUCCESS_CODE = 200

@request_bp.route('/request/1', methods=['GET'])
def request_1():
    return jsonify({"code": SUCCESS_CODE, "data": "request-1"})

@request_bp.route('/request/2', methods=['GET'])
def request_2():
    return jsonify({"code": SUCCESS_CODE, "data": "request-2"})

@request_bp.route('/request/3', methods=['GET'])
def request_3():
    return jsonify({"code": SUCCESS_CODE, "data": "request-3"})

@request_bp.route('/request/4', methods=['GET'])
def request_4():
    return jsonify({"code": SUCCESS_CODE, "data": "request-4"})

@request_bp.route('/request/5', methods=['GET'])
def request_5():
    return jsonify({"code": SUCCESS_CODE, "data": "request-5"})

@request_bp.route('/request/expired', methods=['GET'])
def expired():
    return jsonify({"code": 401, "message": "token expired"}), 401
