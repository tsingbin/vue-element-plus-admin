"""
Menu API - 菜单列表
"""
from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import MenuModel
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/menu", tags=["menu"])

SUCCESS_CODE = 0


def build_menu_tree(menus: List[MenuModel], parent_id: Optional[int] = None) -> List[dict]:
    """构建菜单树形结构"""
    result = []
    for menu in menus:
        if menu.parent_id == parent_id:
            menu_dict = {
                "path": menu.path,
                "component": menu.component,
                "redirect": menu.redirect,
                "name": menu.name,
                "status": menu.status,
                "id": menu.id,
                "type": menu.type,
                "parentId": menu.parent_id,
                "title": menu.title,
                "meta": menu.meta or {}
            }
            # 递归获取子菜单
            children = build_menu_tree(menus, menu.id)
            if children:
                menu_dict["children"] = children
            result.append(menu_dict)
    return result


@router.get("/list", response_model=BaseResponse)
async def get_menu_list(db: Session = Depends(get_db)):
    """获取菜单列表"""
    menus = db.query(MenuModel).order_by(MenuModel.id).all()
    menu_tree = build_menu_tree(menus)
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": menu_tree
        }
    )