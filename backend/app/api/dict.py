"""
Dict API - 字典列表、单个字典
"""
from collections import defaultdict
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import DictModel
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/dict", tags=["dict"])

SUCCESS_CODE = 0


@router.get("/list", response_model=BaseResponse)
async def get_dict_list(db: Session = Depends(get_db)):
    """获取所有字典"""
    dicts = db.query(DictModel).all()
    
    # 按字典类型分组
    dict_obj = defaultdict(list)
    for d in dicts:
        dict_obj[d.dict_type].append({
            "value": int(d.value) if d.value.isdigit() else d.value,
            "label": d.label
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data=dict(dict_obj)
    )


@router.get("/one", response_model=BaseResponse)
async def get_dict_one(db: Session = Depends(get_db)):
    """获取某个字典"""
    dicts = db.query(DictModel).filter(DictModel.dict_type == "test").all()
    
    result = []
    for d in dicts:
        result.append({
            "label": d.label,
            "value": int(d.value) if d.value.isdigit() else d.value
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data=result
    )