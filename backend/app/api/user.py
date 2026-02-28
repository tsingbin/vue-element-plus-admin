"""
User API - 登录、登出、用户列表
"""
import json
from typing import Optional
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import UserModel
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/user", tags=["user"])

SUCCESS_CODE = 0


@router.get("/list", response_model=BaseResponse)
async def get_user_list(
    username: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10),
    db: Session = Depends(get_db)
):
    """获取用户列表"""
    query = db.query(UserModel)
    
    if username:
        query = query.filter(UserModel.username.like(f"%{username}%"))
    
    total = query.count()
    users = query.offset((pageIndex - 1) * pageSize).limit(pageSize).all()
    
    user_list = []
    for user in users:
        user_list.append({
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "roleId": user.role_id,
            "permissions": json.loads(user.permissions) if user.permissions else []
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": total,
            "list": user_list
        }
    )


@router.post("/login", response_model=BaseResponse)
async def login(data: dict, db: Session = Depends(get_db)):
    """用户登录"""
    username = data.get("username")
    password = data.get("password")
    
    user = db.query(UserModel).filter(
        UserModel.username == username,
        UserModel.password == password
    ).first()
    
    if user:
        return BaseResponse(
            code=SUCCESS_CODE,
            data={
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "roleId": user.role_id,
                "permissions": json.loads(user.permissions) if user.permissions else []
            }
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