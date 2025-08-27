from flask import Blueprint, request, jsonify
import uuid
from faker import Faker
import random
department_bp = Blueprint('department', __name__)
fake = Faker("zh_CN")

SUCCESS_CODE = 200

def to_any_string():
    return str(uuid.uuid4())

def random_status():
    return random.randint(0, 1)

# Initialize department list
citys = ['厦门总公司', '北京分公司', '上海分公司', '福州分公司', '深圳分公司', '杭州分公司']
department_list = []

for i in range(5):
    department_list.append({
        "departmentName": citys[i],
        "id": to_any_string(),
        "createTime": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
        "status": random_status(),
        "remark": fake.text(max_nb_chars=15),
        "children": [
            {
                "departmentName": name,
                "id": to_any_string(),
                "createTime": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
                "status": random_status(),
                "remark": fake.text(max_nb_chars=15)
            }
            for name in ["研发部", "产品部", "运营部", "市场部", "销售部", "客服部"]
        ]
    })

@department_bp.route('/list', methods=['GET'])
def department_list_api():
    return jsonify({"code": SUCCESS_CODE, "data": {"list": department_list}})

@department_bp.route('/table/list', methods=['GET'])
def department_table_list():
    return jsonify({"code": SUCCESS_CODE, "data": {"list": department_list, "total": 5}})

@department_bp.route('/users', methods=['GET'])
def department_users():
    page_size = int(request.args.get("pageSize", 10))
    mock_list = []
    for _ in range(page_size):
        mock_list.append({
            "username": fake.name(),
            "account": fake.first_name(),
            "email": fake.email(),
            "createTime": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
            "id": to_any_string()
        })
    return jsonify({"code": SUCCESS_CODE, "data": {"total": 100, "list": mock_list}})

@department_bp.route('/user/save', methods=['POST'])
def save_user():
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

@department_bp.route('/user/delete', methods=['POST'])
def delete_user():
    ids = request.json.get("ids")
    if not ids:
        return jsonify({"code": 500, "message": "请选择需要删除的数据"})
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

@department_bp.route('/save', methods=['POST'])
def save_department():
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

@department_bp.route('/delete', methods=['POST'])
def delete_department():
    ids = request.json.get("ids")
    if not ids:
        return jsonify({"code": 500, "message": "请选择需要删除的数据"})
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
