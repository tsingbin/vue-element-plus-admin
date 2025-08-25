from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

dict_bp = Blueprint('dict', __name__)

# Mock data structure
dict_list = []
dict_types = ['系统字典', '业务字典', '用户字典']

for i in range(1, 6):
    dict_list.append({
        'id': i,
        'dictName': f"字典{i}",
        'dictType': random.choice(dict_types),
        'status': random.randint(0, 1),
        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15))),
        'dictData': [
            {
                'id': i * 10 + j,
                'dictLabel': f"字典项{j}",
                'dictValue': f"value{j}",
                'dictSort': j,
                'status': random.randint(0, 1),
                'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            } for j in range(1, 4)
        ]
    })

SUCCESS_CODE = 200

@dict_bp.route('/list', methods=['GET'])
def get_dict_list():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': dict_list
        }
    })

@dict_bp.route('/data/list', methods=['GET'])
def get_dict_data_list():
    dict_type = request.args.get('dictType')
    data = next((item['dictData'] for item in dict_list if item['dictType'] == dict_type), [])
    return jsonify({
        'code': SUCCESS_CODE,
        'data': data
    })

@dict_bp.route('/save', methods=['POST'])
def save_dict():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@dict_bp.route('/delete', methods=['POST'])
def delete_dict():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })
