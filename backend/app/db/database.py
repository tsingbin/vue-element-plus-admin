"""
数据库连接配置
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 数据库配置
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "vepa_admin")

# 构建数据库连接 URL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

# 创建数据库引擎
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False  # 设置为 True 可以看到 SQL 语句
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()


def get_db():
    """获取数据库会话的依赖函数"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """初始化数据库（创建所有表并初始化种子数据）"""
    from app.db import models  # 导入模型以确保表被创建
    Base.metadata.create_all(bind=engine)
    
    # 初始化种子数据
    from app.db.init_db import init_users, init_menus, init_roles, init_dicts, init_departments, init_examples, init_cards
    
    db = SessionLocal()
    try:
        init_users(db)
        init_menus(db)
        init_roles(db)
        init_dicts(db)
        init_departments(db)
        init_examples(db)
        init_cards(db)
    except Exception as e:
        print(f"种子数据初始化失败: {e}")
    finally:
        db.close()
