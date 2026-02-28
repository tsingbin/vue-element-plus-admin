"""
Department API - 部门列表、用户、保存、删除
"""
import uuid
import random
from typing import List, Optional
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import DepartmentModel, DepartmentUserModel
from app.models.schemas import BaseResponse, DeleteRequest

router = APIRouter(prefix="/department", tags=["department"])

SUCCESS_CODE = 0


def to_any_string():
    """生成随机字符串 ID"""
    return str(uuid.uuid4())


def build_department_tree(departments: List[DepartmentModel], parent_id: Optional[str] = None) -> List[dict]:
    """构建部门树形结构"""
    result = []
    for dept in departments:
        if dept.parent_id == parent_id:
            dept_dict = {
                "departmentName": dept.department_name,
                "id": dept.id,
                "createTime": dept.create_time.strftime("%Y-%m-%d %H:%M:%S") if dept.create_time else None,
                "status": dept.status,
                "remark": dept.remark
            }
            # 递归获取子部门
            children = build_department_tree(departments, dept.id)
            if children:
                dept_dict["children"] = children
            result.append(dept_dict)
    return result


@router.get("/list", response_model=BaseResponse)
async def get_department_list(db: Session = Depends(get_db)):
    """获取部门列表"""
    departments = db.query(DepartmentModel).all()
    dept_tree = build_department_tree(departments)
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": dept_tree
        }
    )


@router.get("/table/list", response_model=BaseResponse)
async def get_department_table_list(db: Session = Depends(get_db)):
    """获取部门表格列表"""
    departments = db.query(DepartmentModel).filter(DepartmentModel.parent_id == None).all()
    dept_tree = build_department_tree(departments)
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": dept_tree,
            "total": len(departments)
        }
    )


@router.get("/users", response_model=BaseResponse)
async def get_users_by_department(
    pageSize: int = Query(10),
    db: Session = Depends(get_db)
):
    """根据部门获取用户列表"""
    users = db.query(DepartmentUserModel).limit(pageSize).all()
    
    user_list = []
    for user in users:
        user_list.append({
            "username": user.username,
            "account": user.account,
            "email": user.email,
            "createTime": user.create_time.strftime("%Y-%m-%d %H:%M:%S") if user.create_time else None,
            "id": user.id
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": db.query(DepartmentUserModel).count(),
            "list": user_list
        }
    )


@router.post("/user/save", response_model=BaseResponse)
async def save_user(data: dict, db: Session = Depends(get_db)):
    """保存用户"""
    user_id = data.get("id")
    
    if user_id:
        user = db.query(DepartmentUserModel).filter(DepartmentUserModel.id == user_id).first()
        if user:
            if data.get("username"):
                user.username = data["username"]
            if data.get("account"):
                user.account = data["account"]
            if data.get("email"):
                user.email = data["email"]
    else:
        user = DepartmentUserModel(
            department_id=data.get("department_id", ""),
            username=data.get("username", ""),
            account=data.get("account", ""),
            email=data.get("email", "")
        )
        db.add(user)
    
    db.commit()
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/user/delete", response_model=BaseResponse)
async def delete_user(data: DeleteRequest, db: Session = Depends(get_db)):
    """删除用户"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    
    db.query(DepartmentUserModel).filter(DepartmentUserModel.id.in_(data.ids)).delete()
    db.commit()
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/save", response_model=BaseResponse)
async def save_department(data: dict, db: Session = Depends(get_db)):
    """保存部门"""
    dept_id = data.get("id")
    
    if dept_id:
        dept = db.query(DepartmentModel).filter(DepartmentModel.id == dept_id).first()
        if dept:
            if data.get("departmentName"):
                dept.department_name = data["departmentName"]
            if data.get("status") is not None:
                dept.status = data["status"]
            if data.get("remark"):
                dept.remark = data["remark"]
    else:
        dept = DepartmentModel(
            id=to_any_string(),
            department_name=data.get("departmentName", ""),
            parent_id=data.get("parentId"),
            status=data.get("status", 1),
            remark=data.get("remark", "")
        )
        db.add(dept)
    
    db.commit()
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/delete", response_model=BaseResponse)
async def delete_department(data: DeleteRequest, db: Session = Depends(get_db)):
    """删除部门"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    
    db.query(DepartmentModel).filter(DepartmentModel.id.in_(data.ids)).delete()
    db.commit()
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )