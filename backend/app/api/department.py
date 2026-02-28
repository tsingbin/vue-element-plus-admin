"""
Department API - 部门列表、用户、保存、删除
"""
import uuid
import random
from typing import List, Optional
from fastapi import APIRouter, Query
from app.models.schemas import BaseResponse, DeleteRequest, SaveUserRequest, SaveDepartmentRequest

router = APIRouter(prefix="/department", tags=["department"])

SUCCESS_CODE = 0


def to_any_string():
    """生成随机字符串 ID"""
    return str(uuid.uuid4())


# 部门列表数据
CITIES = ['厦门总公司', '北京分公司', '上海分公司', '福州分公司', '深圳分公司', '杭州分公司']

# 存储部门数据
DEPARTMENT_LIST = []

for i in range(5):
    DEPARTMENT_LIST.append({
        "departmentName": CITIES[i],
        "id": to_any_string(),
        "createTime": "2024-01-01 12:00:00",
        "status": random.randint(0, 1),
        "remark": "这是一个备注信息",
        "children": [
            {
                "departmentName": "研发部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            },
            {
                "departmentName": "产品部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            },
            {
                "departmentName": "运营部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            },
            {
                "departmentName": "市场部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            },
            {
                "departmentName": "销售部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            },
            {
                "departmentName": "客服部",
                "id": to_any_string(),
                "createTime": "2024-01-01 12:00:00",
                "status": random.randint(0, 1),
                "remark": "这是一个备注信息"
            }
        ]
    })


# 模拟用户名列表
FIRST_NAMES = ['张', '李', '王', '刘', '陈', '杨', '赵', '黄', '周', '吴']
LAST_NAMES = ['伟', '芳', '娜', '敏', '静', '丽', '强', '磊', '军', '洋', '勇', '艳', '杰', '涛', '明', '超', '秀英', '华', '平', '刚']


def generate_mock_users(page_size: int):
    """生成模拟用户数据"""
    mock_list = []
    for i in range(page_size):
        mock_list.append({
            "username": random.choice(FIRST_NAMES) + random.choice(LAST_NAMES),
            "account": f"user_{random.randint(100, 999)}",
            "email": f"user{random.randint(100, 999)}@example.com",
            "createTime": "2024-01-01 12:00:00",
            "id": to_any_string()
        })
    return mock_list


@router.get("/list", response_model=BaseResponse)
async def get_department_list():
    """获取部门列表"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": DEPARTMENT_LIST
        }
    )


@router.get("/table/list", response_model=BaseResponse)
async def get_department_table_list():
    """获取部门表格列表"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": DEPARTMENT_LIST,
            "total": len(DEPARTMENT_LIST)
        }
    )


@router.get("/users", response_model=BaseResponse)
async def get_users_by_department(
    pageSize: int = Query(10, alias="pageSize")
):
    """根据部门获取用户列表"""
    mock_list = generate_mock_users(pageSize)
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": 100,
            "list": mock_list
        }
    )


@router.post("/user/save", response_model=BaseResponse)
async def save_user(data: SaveUserRequest):
    """保存用户"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/user/delete", response_model=BaseResponse)
async def delete_user(data: DeleteRequest):
    """删除用户"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/save", response_model=BaseResponse)
async def save_department(data: SaveDepartmentRequest):
    """保存部门"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/delete", response_model=BaseResponse)
async def delete_department(data: DeleteRequest):
    """删除部门"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )
