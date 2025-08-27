from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import string

menu_bp = Blueprint('menu', __name__)


SUCCESS_CODE = 200

def random_status():
    return random.randint(0, 1)

@menu_bp.route('/menu/list', methods=['GET'])
def menu_list():
    data = {
        "list": [
            {
                "path": "/dashboard",
                "component": "#",
                "redirect": "/dashboard/analysis",
                "name": "Dashboard",
                "status": random_status(),
                "id": 1,
                "type": 0,
                "parentId": None,
                "title": "首页",
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
                        "type": 1,
                        "parentId": 1,
                        "title": "分析页",
                        "permissionList": [
                            {"id": 1, "label": "新增", "value": "add"},
                            {"id": 2, "label": "编辑", "value": "edit"}
                        ],
                        "meta": {"title": "分析页", "noCache": True, "permission": ["add", "edit"]}
                    },
                    {
                        "path": "workplace",
                        "component": "views/Dashboard/Workplace",
                        "name": "Workplace",
                        "status": random_status(),
                        "id": 3,
                        "type": 1,
                        "parentId": 1,
                        "title": "工作台",
                        "permissionList": [
                            {"id": 1, "label": "新增", "value": "add"},
                            {"id": 2, "label": "编辑", "value": "edit"},
                            {"id": 3, "label": "删除", "value": "delete"}
                        ],
                        "meta": {"title": "工作台", "noCache": True}
                    }
                ]
            },
            {
                "path": "/external-link",
                "component": "#",
                "meta": {"title": "文档", "icon": "vi-clarity:document-solid"},
                "name": "ExternalLink",
                "status": random_status(),
                "id": 4,
                "type": 0,
                "parentId": None,
                "title": "文档",
                "children": [
                    {
                        "path": "https://element-plus-admin-doc.cn/",
                        "name": "DocumentLink",
                        "status": random_status(),
                        "id": 5,
                        "type": 1,
                        "parentId": 4,
                        "title": "文档",
                        "meta": {"title": "文档"}
                    }
                ]
            },
            # You can continue adding other nested menu items in the same pattern...
        ]
    }

    return jsonify({"code": SUCCESS_CODE, "data": data})