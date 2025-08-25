from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

table_bp = Blueprint('table', __name__)

# Mock data structure
table_list = []
status_list = ['published', 'draft', 'deleted']
authors = ['王小明', '李小红', '张小花', '刘小刚', '陈小强']

for i in range(1, 21):
    table_list.append({
        'id': i,
        'title': f"标题{i}",
        'author': random.choice(authors),
        'status': random.choice(status_list),
        'pageviews': random.randint(100, 1000),
        'createTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'remark': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(10, 15)))
    })

SUCCESS_CODE = 200

@table_bp.route('/list', methods=['GET'])
def get_table_list():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))
    
    start = (page - 1) * page_size
    end = start + page_size
    
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'list': table_list[start:end],
            'total': len(table_list)
        }
    })

@table_bp.route('/save', methods=['POST'])
def save_table():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })

@table_bp.route('/delete', methods=['POST'])
def delete_table():
    if not request.json or 'ids' not in request.json:
        return jsonify({
            'code': 500,
            'message': '请选择需要删除的数据'
        }), 500
    return jsonify({
        'code': SUCCESS_CODE,
        'data': 'success'
    })
