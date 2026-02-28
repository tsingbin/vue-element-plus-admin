"""
Workplace API - 工作台数据
"""
from datetime import datetime
from fastapi import APIRouter
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/workplace", tags=["workplace"])

SUCCESS_CODE = 0


@router.get("/total", response_model=BaseResponse)
async def get_total():
    """获取统计数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "project": 40,
            "access": 2340,
            "todo": 10
        }
    )


@router.get("/project", response_model=BaseResponse)
async def get_project():
    """获取项目数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {
                "name": "Github",
                "icon": "akar-icons:github-fill",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Vue",
                "icon": "logos:vue",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Angular",
                "icon": "logos:angular-icon",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "React",
                "icon": "logos:react",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Webpack",
                "icon": "logos:webpack",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            },
            {
                "name": "Vite",
                "icon": "vscode-icons:file-type-vite",
                "message": "workplace.introduction",
                "personal": "Archer",
                "time": datetime.now().isoformat()
            }
        ]
    )


@router.get("/dynamic", response_model=BaseResponse)
async def get_dynamic():
    """获取动态数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            },
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            },
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            },
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            },
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            },
            {
                "keys": ["workplace.push", "Github"],
                "time": datetime.now().isoformat()
            }
        ]
    )


@router.get("/team", response_model=BaseResponse)
async def get_team():
    """获取团队信息"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {
                "name": "Github",
                "icon": "akar-icons:github-fill"
            },
            {
                "name": "Vue",
                "icon": "logos:vue"
            },
            {
                "name": "Angular",
                "icon": "logos:angular-icon"
            },
            {
                "name": "React",
                "icon": "logos:react"
            },
            {
                "name": "Webpack",
                "icon": "logos:webpack"
            },
            {
                "name": "Vite",
                "icon": "vscode-icons:file-type-vite"
            }
        ]
    )


@router.get("/radar", response_model=BaseResponse)
async def get_radar():
    """获取指数数据"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=[
            {"name": "workplace.quote", "max": 65, "personal": 42, "team": 50},
            {"name": "workplace.contribution", "max": 160, "personal": 30, "team": 140},
            {"name": "workplace.hot", "max": 300, "personal": 20, "team": 28},
            {"name": "workplace.yield", "max": 130, "personal": 35, "team": 35},
            {"name": "workplace.follow", "max": 100, "personal": 80, "team": 90}
        ]
    )
