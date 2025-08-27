from flask import Blueprint, request, jsonify
import random
from datetime import datetime

role_bp = Blueprint('role', __name__)

SUCCESS_CODE = 200

# Generate random status (0 or 1)
def random_status():
    return random.randint(0, 1)

# Example of simplified route structure (adminList equivalent)
admin_list = [
    {
        "path": "/dashboard",
        "component": "#",
        "redirect": "/dashboard/analysis",
        "name": "Dashboard",
        "meta": {
            "title": "router.dashboard",
            "icon": "vi-ant-design:dashboard-filled",
            "alwaysShow": True
        },
        "children": [
            {
                "path": "analysis",
                "component": "views/Dashboard/Analysis",
                "name": "Analysis",
                "meta": {
                    "title": "router.analysis",
                    "noCache": True,
                    "affix": True
                }
            },
            {
                "path": "workplace",
                "component": "views/Dashboard/Workplace",
                "name": "Workplace",
                "meta": {
                    "title": "router.workplace",
                    "noCache": True,
                    "affix": True
                }
            }
        ]
    }
    # Add more items like external-link, components, etc.
]

# Role-based menus (similar to menus in TS)
menus = [
    [
        {
            "path": "/dashboard",
            "component": "#",
            "redirect": "/dashboard/analysis",
            "name": "Dashboard",
            "status": random_status(),
            "id": 1,
            "meta": {
                "title": "首页",
                "icon": "vi-ant-design:dashboard-filled",
                "alwaysShow": True
            },
            "children": [
                {
                    "path": "analysis",
                    "component": "views/Dashboard/Analysis",
                    "name": "Analysis",
                    "status": random_status(),
                    "id": 2,
                    "meta": {
                        "title": "分析页",
                        "noCache": True
                    }
                },
                {
                    "path": "workplace",
                    "component": "views/Dashboard/Workplace",
                    "name": "Workplace",
                    "status": random_status(),
                    "id": 3,
                    "meta": {
                        "title": "工作台",
                        "noCache": True
                    }
                }
            ]
        }
    ]
]

# Endpoint to return menu list based on role
@role_bp.route('/list', methods=['GET'])
def get_menu_list():
    role = request.args.get('role', '0')  # default role 0
    try:
        role_index = int(role)
    except ValueError:
        role_index = 0

    role_index = min(role_index, len(menus) - 1)
    return jsonify({
        "code": SUCCESS_CODE,
        "data": menus[role_index]
    })

# Endpoint to return all admin routes (like adminList in TS)
@role_bp.route('/admin-list', methods=['GET'])
def get_admin_list():
    return jsonify({
        "code": SUCCESS_CODE,
        "data": admin_list
    })
