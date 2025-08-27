from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

dict_bp = Blueprint('dict', __name__)
from flask import Flask, jsonify
import time


SUCCESS_CODE = 200
TIMEOUT = 1  # 1 second

# Dictionary data
dict_obj = {
    "importance": [
        {"value": 0, "label": "tableDemo.commonly"},
        {"value": 1, "label": "tableDemo.good"},
        {"value": 2, "label": "tableDemo.important"}
    ]
}

# Route for dictionary list
@dict_bp.route('/list', methods=['GET'])
def get_dict_list():
    time.sleep(TIMEOUT)  # simulate delay
    return jsonify({
        "code": SUCCESS_CODE,
        "data": dict_obj
    })

# Route for single dictionary
@dict_bp.route('/one', methods=['GET'])
def get_one_dict():
    time.sleep(TIMEOUT)  # simulate delay
    return jsonify({
        "code": SUCCESS_CODE,
        "data": [
            {"label": "test1", "value": 0},
            {"label": "test2", "value": 1},
            {"label": "test3", "value": 2}
        ]
    })
