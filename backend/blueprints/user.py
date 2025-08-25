from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)

SUCCESS_CODE = 200

# Mock user data
users = [
    {
        'username': 'admin',
        'password': 'admin',
        'role': 'admin',
        'roleId': '1',
        'permissions': ['*.*.*']
    },
    {
        'username': 'test',
        'password': 'test',
        'role': 'test',
        'roleId': '2',
        'permissions': ['example:dialog:create', 'example:dialog:delete']
    }
]

@user_bp.route('/list', methods=['GET'])
def get_user_list():
    username = request.args.get('username')
    page_index = int(request.args.get('pageIndex', 1))
    page_size = int(request.args.get('pageSize', 10))

    filtered_users = [user for user in users 
                     if not username or username in user['username']]
    
    start = (page_index - 1) * page_size
    end = start + page_size
    paginated_users = filtered_users[start:end]
    
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'total': len(filtered_users),
            'list': paginated_users
        }
    })

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({
                'code': SUCCESS_CODE,
                'data': user
            })
    
    return jsonify({
        'code': 500,
        'message': '账号或密码错误'
    }), 500

@user_bp.route('/loginOut', methods=['GET'])
def logout():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': None
    })
