"""
FastAPI Main Application
Vue Element Plus Admin Backend API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import user, menu, role, dict, department, table, request, analysis, workplace

# 创建 FastAPI 应用
app = FastAPI(
    title="Vue Element Plus Admin API",
    description="Backend API for Vue Element Plus Admin",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头部
)

# 注册路由
app.include_router(user.router, prefix="/api")
app.include_router(menu.router, prefix="/api")
app.include_router(role.router, prefix="/api")
app.include_router(dict.router, prefix="/api")
app.include_router(department.router, prefix="/api")
app.include_router(table.router, prefix="/api")
app.include_router(table.card_router, prefix="/api")
app.include_router(request.router, prefix="/api")
app.include_router(analysis.router, prefix="/api")
app.include_router(workplace.router, prefix="/api")


@app.get("/")
async def root():
    """根路径"""
    return {"message": "Vue Element Plus Admin API is running"}


@app.get("/health")
async def health():
    """健康检查"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
