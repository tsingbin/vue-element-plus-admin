from flask import Blueprint, request, jsonify
import random
from datetime import datetime, timedelta
import string

request_bp = Blueprint('request', __name__)

# Mock data structure
request_list = []
status_list = ['pending', 'processing', 'completed', 'rejected']
request_types = ['数据请求', 'API访问', '系统配置', '权限申请']

for i in range(1, 21):
    request_list.append({
        'id': i,
        'requestType': random.choice(request_types),
        'requestName': f"请求{i}",
        'requestUser': random.choice(['张三', '李四', '王五']),
        'requestTime': (datetime.now() - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S'),
        'status': random.choice(status_list),
        'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15)))
    })

SUCCESS_CODE = 200

@request_bp.route('/list', methods=['GET'])
def get_request_list():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))
    
    start = (page - 1) * page_size
    end = start + page_size
    
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': request_list[start:end],
            'total': len(request_list)
        }
    })

@request_bp.route('/save', methods=['POST'])
def save_request():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@request_bp.route('/delete', methods=['POST'])
def delete_request():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@request_bp.route('/status', methods=['GET'])
def get_status_count():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'pending': len([r for r in request_list if r['status'] == 'pending']),
            'processing': len([r for r in request_list if r['status'] == 'processing']),
            'completed': len([r for r in request_list if r['status'] == 'completed']),
            'rejected': len([r for r in request_list if r['status'] == 'rejected'])
        }
    })
