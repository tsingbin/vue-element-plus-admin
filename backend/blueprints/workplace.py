from flask import Blueprint, request, jsonify
import random
from datetime import datetime, timedelta
import string

workplace_bp = Blueprint('workplace', __name__)

SUCCESS_CODE = 200  # Same as SUCCESS_CODE in TS

# 获取统计
@workplace_bp.route('/total', methods=['GET'])
def get_total():
    return jsonify({
        "code": SUCCESS_CODE,
        "data": {
            "project": 40,
            "access": 230,
            "todo": 10
        }
    })

# 获取项目
@workplace_bp.route('/project', methods=['GET'])
def get_project():
    return jsonify({
        "code": SUCCESS_CODE,
        "data": [
            {
                "name": "Github",
                "icon": "akar-icons:github-fill",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Vue",
                "icon": "logos:vue",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Angular",
                "icon": "logos:angular-icon",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "React",
                "icon": "logos:react",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Webpack",
                "icon": "logos:webpack",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Vite",
                "icon": "vscode-icons:file-type-vite",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            }
        ]
    })

# 获取动态
@workplace_bp.route('/dynamic', methods=['GET'])
def get_dynamic():
    data = [{"keys": ["workplace.push", "Github"], "time": datetime.now().isoformat()} for _ in range(6)]
    return jsonify({
        "code": SUCCESS_CODE,
        "data": data
    })

# 获取团队信息
@workplace_bp.route('/team', methods=['GET'])
def get_team():
    return jsonify({
        "code": SUCCESS_CODE,
        "data": [
            {"name": "Github", "icon": "akar-icons:github-fill"},
            {"name": "Vue", "icon": "logos:vue"},
            {"name": "Angular", "icon": "logos:angular-icon"},
            {"name": "React", "icon": "logos:react"},
            {"name": "Webpack", "icon": "logos:webpack"},
            {"name": "Vite", "icon": "vscode-icons:file-type-vite"}
        ]
    })

# 获取指数
@workplace_bp.route('/radar', methods=['GET'])
def get_radar():
    return jsonify({
        "code": SUCCESS_CODE,
        "data": [
            {"name": "workplace.quote", "max": 65, "personal": 42, "team": 50},
            {"name": "workplace.contribution", "max": 160, "personal": 30, "team": 140},
            {"name": "workplace.hot", "max": 300, "personal": 20, "team": 28},
            {"name": "workplace.yield", "max": 130, "personal": 35, "team": 35},
            {"name": "workplace.follow", "max": 100, "personal": 80, "team": 90}
        ]
    })
