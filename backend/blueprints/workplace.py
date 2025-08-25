from flask import Blueprint, request, jsonify
import random
from datetime import datetime, timedelta
import string

workplace_bp = Blueprint('workplace', __name__)

# Mock data structure
projects = [
    {'name': '项目A', 'percent': random.randint(80, 100)},
    {'name': '项目B', 'percent': random.randint(60, 90)},
    {'name': '项目C', 'percent': random.randint(40, 80)},
    {'name': '项目D', 'percent': random.randint(20, 60)},
    {'name': '项目E', 'percent': random.randint(0, 40)}
]

activities = [
    {
        'id': i,
        'content': f"活动内容{i}",
        'time': (datetime.now() - timedelta(hours=i)).strftime('%H:%M'),
        'user': random.choice(['张三', '李四', '王五'])
    } for i in range(1, 6)
]

teams = [
    {
        'id': i,
        'name': f"团队成员{i}",
        'avatar': f"https://randomuser.me/api/portraits/{random.choice(['men', 'women'])}/{i}.jpg"
    } for i in range(1, 6)
]

SUCCESS_CODE = 200

@workplace_bp.route('/projects', methods=['GET'])
def get_projects():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': projects
    })

@workplace_bp.route('/activities', methods=['GET'])
def get_activities():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': activities
    })

@workplace_bp.route('/teams', methods=['GET'])
def get_teams():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': teams
    })

@workplace_bp.route('/radar', methods=['GET'])
def get_radar_data():
    return jsonify({
        'code': SUCCESS_CODE,
        'data': {
            'indicator': [
                {'name': '引用', 'max': 100},
                {'name': '热度', 'max': 100},
                {'name': '产量', 'max': 100},
                {'name': '贡献', 'max': 100},
                {'name': '热度', 'max': 100}
            ],
            'value': [random.randint(50, 100) for _ in range(5)]
        }
    })
