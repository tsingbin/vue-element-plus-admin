from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

department_bp = Blueprint('department', __name__)

# Mock data structure
department_list = []
citys = ['厦门总公司', '北京分公司', '上海分公司', '福州分公司', '深圳分公司', '杭州分公司']

for i in range(5):
    department_list.append({
        'departmentName': citys[i],
        'id': ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'status': random.randint(0, 1),
        'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15))),
        'children': [
            {
                'departmentName': dept,
                'id': ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
                'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'status': random.randint(0, 1),
                'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15)))
            } for dept in ['研发部', '产品部', '运营部', '市场部', '销售部', '客服部']
        ]
    })

SUCCESS_CODE = 200

@department_bp.route('/list', methods=['GET'])
def get_department_list():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': department_list
        }
    })

@department_bp.route('/table/list', methods=['GET'])
def get_department_table():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': department_list,
            'total': 5
        }
    })

@department_bp.route('/users', methods=['GET'])
def get_department_users():
    page_size = int(request.args.get('pageSize', 10))
    mock_list = []
    for _ in range(page_size):
        mock_list.append({
            'username': ''.join(random.choices('赵钱孙李周吴郑王', k=2)),
            'account': ''.join(random.choices(string.ascii_lowercase, k=6)),
            'email': f"{''.join(random.choices(string.ascii_lowercase, k=8))}@example.com",
            'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'id': ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        })
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'total': 100,
            'list': mock_list
        }
    })

@department_bp.route('/user/save', methods=['POST'])
def save_user():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@department_bp.route('/user/delete', methods=['POST'])
def delete_user():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@department_bp.route('/save', methods=['POST'])
def save_department():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@department_bp.route('/delete', methods=['POST'])
def delete_department():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })
