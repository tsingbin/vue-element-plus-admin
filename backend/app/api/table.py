"""
Example/Table API - 表格列表、树形列表、卡片列表、保存、详情、删除
"""
import uuid
import random
from typing import List, Optional
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import ExampleModel, CardModel
from app.models.schemas import BaseResponse, DeleteRequest

router = APIRouter(prefix="/example", tags=["example"])

SUCCESS_CODE = 0


def to_any_string():
    """生成随机字符串 ID"""
    return str(uuid.uuid4())


def build_example_tree(examples: List[ExampleModel], parent_id: Optional[str] = None) -> List[dict]:
    """构建树形结构"""
    result = []
    for example in examples:
        if example.parent_id == parent_id:
            example_dict = {
                "id": example.id,
                "author": example.author,
                "title": example.title,
                "content": example.content,
                "importance": example.importance,
                "display_time": example.display_time,
                "pageviews": example.pageviews,
                "image_uri": example.image_uri,
                "video_uri": example.video_uri
            }
            children = build_example_tree(examples, example.id)
            if children:
                example_dict["children"] = children
            result.append(example_dict)
    return result


@router.get("/list", response_model=BaseResponse)
async def get_table_list(
    title: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10),
    db: Session = Depends(get_db)
):
    """获取表格列表"""
    query = db.query(ExampleModel).filter(ExampleModel.parent_id == None)
    
    if title:
        query = query.filter(ExampleModel.title.like(f"%{title}%"))
    
    total = query.count()
    examples = query.offset((pageIndex - 1) * pageSize).limit(pageSize).all()
    
    example_list = []
    for e in examples:
        example_list.append({
            "id": e.id,
            "author": e.author,
            "title": e.title,
            "content": e.content,
            "importance": e.importance,
            "display_time": e.display_time,
            "pageviews": e.pageviews,
            "image_uri": e.image_uri,
            "video_uri": e.video_uri
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": total,
            "list": example_list
        }
    )


@router.get("/treeList", response_model=BaseResponse)
async def get_tree_table_list(
    title: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10),
    db: Session = Depends(get_db)
):
    """获取树形表格列表"""
    query = db.query(ExampleModel)
    
    if title:
        query = query.filter(ExampleModel.title.like(f"%{title}%"))
    
    examples = query.all()
    tree_list = build_example_tree(examples)
    
    # 分页
    start = (pageIndex - 1) * pageSize
    end = pageIndex * pageSize
    page_list = tree_list[start:end]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": len(tree_list),
            "list": page_list
        }
    )


@router.get("/detail", response_model=BaseResponse)
async def get_table_detail(id: str = Query(...), db: Session = Depends(get_db)):
    """获取表格详情"""
    example = db.query(ExampleModel).filter(ExampleModel.id == id).first()
    
    if example:
        return BaseResponse(
            code=SUCCESS_CODE,
            data={
                "id": example.id,
                "author": example.author,
                "title": example.title,
                "content": example.content,
                "importance": example.importance,
                "display_time": example.display_time,
                "pageviews": example.pageviews,
                "image_uri": example.image_uri,
                "video_uri": example.video_uri
            }
        )
    
    return BaseResponse(
        code=404,
        message="数据不存在"
    )


@router.post("/save", response_model=BaseResponse)
async def save_table(data: dict, db: Session = Depends(get_db)):
    """保存表格数据"""
    example_id = data.get("id")
    
    if example_id:
        example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
        if example:
            if data.get("author"):
                example.author = data["author"]
            if data.get("title"):
                example.title = data["title"]
            if data.get("content"):
                example.content = data["content"]
            if data.get("importance"):
                example.importance = data["importance"]
            if data.get("display_time"):
                example.display_time = data["display_time"]
            if data.get("pageviews"):
                example.pageviews = data["pageviews"]
            if data.get("image_uri"):
                example.image_uri = data["image_uri"]
            if data.get("video_uri"):
                example.video_uri = data["video_uri"]
    else:
        example = ExampleModel(
            id=to_any_string(),
            author=data.get("author", ""),
            title=data.get("title", ""),
            content=data.get("content", ""),
            importance=data.get("importance", 1),
            display_time=data.get("display_time", ""),
            pageviews=data.get("pageviews", 0),
            image_uri=data.get("image_uri", ""),
            video_uri=data.get("video_uri", "")
        )
        db.add(example)
    
    db.commit()
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/delete", response_model=BaseResponse)
async def delete_table(data: DeleteRequest, db: Session = Depends(get_db)):
    """删除表格数据"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    
    db.query(ExampleModel).filter(ExampleModel.id.in_(data.ids)).delete()
    db.commit()
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


# 卡片列表路由
card_router = APIRouter(prefix="/card", tags=["card"])


@card_router.get("/list", response_model=BaseResponse)
async def get_card_list(
    name: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10),
    db: Session = Depends(get_db)
):
    """获取卡片列表"""
    query = db.query(CardModel)
    
    if name:
        query = query.filter(CardModel.name.like(f"%{name}%"))
    
    total = query.count()
    cards = query.offset((pageIndex - 1) * pageSize).limit(pageSize).all()
    
    card_list = []
    for card in cards:
        card_list.append({
            "logo": card.logo,
            "name": card.name,
            "desc": card.desc
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": total,
            "list": card_list
        }
    )