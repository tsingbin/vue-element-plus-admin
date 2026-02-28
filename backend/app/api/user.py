"""
User API - 登录、登出、用户列表
"""
from typing import List, Optional
from fastapi import APIRouter, Query
from app.models.schemas import BaseResponse, UserInfo, UserListResponse, UserLogin

router = APIRouter(prefix="/user", tags=["user"])

SUCCESS_CODE = 0

# 模拟用户数据
USER_LIST: List[dict] = [
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


@router.get("/list", response_model=BaseResponse)
async def get_user_list(
    username: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10)
):
    """获取用户列表"""
    mock_list = USER_LIST
    if username:
        mock_list = [item for item in mock_list if username in item["username"]]
    
    start = (pageIndex - 1) * pageSize
    end = pageIndex * pageSize
    page_list = mock_list[start:end]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": len(mock_list),
            "list": page_list
        }
    )


@router.post("/login", response_model=BaseResponse)
async def login(data: UserLogin):
    """用户登录"""
    for user in USER_LIST:
        if user["username"] == data.username and user["password"] == data.password:
            return BaseResponse(
                code=SUCCESS_CODE,
                data=user
            )
    return BaseResponse(
        code=500,
        message="账号或密码错误"
    )


@router.get("/loginOut", response_model=BaseResponse)
async def login_out():
    """用户登出"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=None
    )
