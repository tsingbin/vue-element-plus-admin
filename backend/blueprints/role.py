from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

role_bp = Blueprint('role', __name__)

# Mock data structure
role_list = []
status_list = ['启用', '禁用']

for i in range(1, 6):
    role_list.append({
        'id': i,
        'roleName': f"角色{i}",
        'roleKey': f"role{i}",
        'roleSort': i,
        'status': random.choice(status_list),
        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15))),
        'menuIds': [j for j in range(1, i+3)]
    })

SUCCESS_CODE = 200

@role_bp.route('/list', methods=['GET'])
def get_role_list():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': role_list
        }
    })

@role_bp.route('/table/list', methods=['GET'])
def get_role_table():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': role_list,
            'total': len(role_list)
        }
    })

@role_bp.route('/save', methods=['POST'])
def save_role():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@role_bp.route('/delete', methods=['POST'])
def delete_role():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })
