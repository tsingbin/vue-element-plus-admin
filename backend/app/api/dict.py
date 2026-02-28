"""
Dict API - 字典列表、单个字典
"""
from fastapi import APIRouter
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/dict", tags=["dict"])

SUCCESS_CODE = 0

# 字典数据
DICT_OBJ = {
    "importance": [
        {
            "value": 0,
            "label": "tableDemo.commonly"
        },
        {
            "value": 1,
            "label": "tableDemo.good"
        },
        {
            "value": 2,
            "label": "tableDemo.important"
        }
    ]
}


@router.get("/list", response_model=BaseResponse)
async def get_dict_list():
    """获取所有字典"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=DICT_OBJ
    )


@router.get("/one", response_model=BaseResponse)
async def get_dict_one():
    """获取某个字典"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {
                "label": "test1",
                "value": 0
            },
            {
                "label": "test2",
                "value": 1
            },
            {
                "label": "test3",
                "value": 2
            }
        ]
    )
