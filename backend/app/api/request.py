"""
Request API - 测试请求
"""
from fastapi import APIRouter
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/request", tags=["request"])

SUCCESS_CODE = 0


@router.get("/1", response_model=BaseResponse)
async def request_1():
    """测试请求1"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="request-1"
    )


@router.get("/2", response_model=BaseResponse)
async def request_2():
    """测试请求2"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="request-2"
    )


@router.get("/3", response_model=BaseResponse)
async def request_3():
    """测试请求3"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="request-3"
    )


@router.get("/4", response_model=BaseResponse)
async def request_4():
    """测试请求4"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="request-4"
    )


@router.get("/5", response_model=BaseResponse)
async def request_5():
    """测试请求5"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data="request-5"
    )


@router.get("/expired", response_model=BaseResponse)
async def request_expired():
    """模拟 token 过期"""
    return BaseResponse(
        code=401,
        message="token expired"
    )
