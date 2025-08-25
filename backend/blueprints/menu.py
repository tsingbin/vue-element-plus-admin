from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

menu_bp = Blueprint('menu', __name__)

# Mock data structure
menu_list = []
menu_types = ['目录', '菜单', '按钮']

for i in range(1, 6):
    menu_list.append({
        'id': i,
        'menuName': f"菜单{i}",
        'menuType': random.choice(menu_types),
        'path': f"/menu{i}",
        'component': f"Menu{i}",
        'perms': f"system:menu:list{i}",
        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': random.randint(0, 1),
        'children': [
            {
                'id': i * 10 + j,
                'menuName': f"子菜单{j}",
                'menuType': random.choice(menu_types),
                'path': f"/menu{i}/sub{j}",
                'component': f"SubMenu{j}",
                'perms': f"system:menu:sub:list{j}",
                'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': random.randint(0, 1)
            } for j in range(1, 4)
        ]
    })

SUCCESS_CODE = 200

@menu_bp.route('/list', methods=['GET'])
def get_menu_list():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': menu_list
        }
    })

@menu_bp.route('/save', methods=['POST'])
def save_menu():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@menu_bp.route('/delete', methods=['POST'])
def delete_menu():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })
