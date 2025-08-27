from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)

SUCCESS_CODE = 200
# Mock data
users = [
    {
        "username": "admin",
        "password": "admin",
        "role": "admin",
        "roleId": "1",
        "permissions": ["*.*.*"]
    },
    {
        "username": "test",
        "password": "test",
        "role": "test",
        "roleId": "2",
        "permissions": ["example:dialog:create", "example:dialog:delete"]
    }
]

# ✅ 列表接口
@user_bp.route('/list', methods=['GET'])
def get_user_list():
    username = request.args.get('username', '').strip()
    page_index = int(request.args.get('pageIndex', 1))
    page_size = int(request.args.get('pageSize', 10))

    # Filter by username if provided
    mock_list = [u for u in users if username.lower() in u["username"].lower()] if username else users

    # Pagination
    start = (page_index - 1) * page_size
    end = start + page_size
    page_list = mock_list[start:end]

    return jsonify({
        "code": SUCCESS_CODE,
        "data": {
            "total": len(mock_list),
            "list": page_list
        }
    })

# ✅ 登录接口
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:
            return jsonify({"code": SUCCESS_CODE, "data": user})

    return jsonify({"code": 500, "message": "账号或密码错误"}), 401

# ✅ 退出接口
@user_bp.route('/loginOut', methods=['GET'])
def logout():
    return jsonify({"code": SUCCESS_CODE, "data": None})
