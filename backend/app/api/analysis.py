"""
Analysis API - 分析页统计数据
"""
from fastapi import APIRouter
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/analysis", tags=["analysis"])

SUCCESS_CODE = 0


@router.get("/total", response_model=BaseResponse)
async def get_total():
    """获取统计数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "users": 1,
            "messages": 2,
            "moneys": 3,
            "shoppings": 4
        }
    )


@router.get("/userAccessSource", response_model=BaseResponse)
async def get_user_access_source():
    """获取用户来源数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {"value": 1, "name": "analysis.directAccess"},
            {"value": 2, "name": "analysis.mailMarketing"},
            {"value": 3, "name": "analysis.allianceAdvertising"},
            {"value": 4, "name": "analysis.videoAdvertising"},
            {"value": 5, "name": "analysis.searchEngines"}
        ]
    )


@router.get("/weeklyUserActivity", response_model=BaseResponse)
async def get_weekly_user_activity():
    """获取每周用户活跃量"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {"value": 1, "name": "analysis.monday"},
            {"value": 2, "name": "analysis.tuesday"},
            {"value": 3, "name": "analysis.wednesday"},
            {"value": 4, "name": "analysis.thursday"},
            {"value": 5, "name": "analysis.friday"},
            {"value": 6, "name": "analysis.saturday"},
            {"value": 7, "name": "analysis.sunday"}
        ]
    )


@router.get("/monthlySales", response_model=BaseResponse)
async def get_monthly_sales():
    """获取每月销售额"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {"estimate": 100, "actual": 120, "name": "analysis.january"},
            {"estimate": 120, "actual": 82, "name": "analysis.february"},
            {"estimate": 161, "actual": 91, "name": "analysis.march"},
            {"estimate": 134, "actual": 154, "name": "analysis.april"},
            {"estimate": 105, "actual": 162, "name": "analysis.may"},
            {"estimate": 160, "actual": 140, "name": "analysis.june"},
            {"estimate": 165, "actual": 145, "name": "analysis.july"},
            {"estimate": 114, "actual": 250, "name": "analysis.august"},
            {"estimate": 163, "actual": 134, "name": "analysis.september"},
            {"estimate": 185, "actual": 56, "name": "analysis.october"},
            {"estimate": 118, "actual": 99, "name": "analysis.november"},
            {"estimate": 123, "actual": 123, "name": "analysis.december"}
        ]
    )
