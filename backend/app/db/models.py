"""
SQLAlchemy 数据模型
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.db.database import Base


class UserModel(Base):
    """用户表"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    role_id = Column(String(50), nullable=False)
    permissions = Column(Text, nullable=True)  # JSON 字符串存储权限列表
    status = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class MenuModel(Base):
    """菜单表"""
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    path = Column(String(255), nullable=True)
    component = Column(String(255), nullable=True)
    redirect = Column(String(255), nullable=True)
    name = Column(String(100), nullable=True)
    status = Column(Integer, default=1)
    type = Column(Integer, default=0)  # 0: 目录, 1: 菜单
    parent_id = Column(Integer, ForeignKey("menus.id"), nullable=True)
    title = Column(String(100), nullable=True)
    icon = Column(String(100), nullable=True)
    meta = Column(JSON, nullable=True)  # 存储额外的 meta 信息
    permission = Column(Text, nullable=True)  # JSON 字符串存储权限列表
    sort = Column(Integer, default=0)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # 自关联
    children = relationship("MenuModel", backref="parent", remote_side=[id])


class RoleModel(Base):
    """角色表"""
    __tablename__ = "roles"

    id = Column(String(50), primary_key=True)
    role_name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    status = Column(Integer, default=1)
    remark = Column(String(255), nullable=True)
    menu = Column(JSON, nullable=True)  # 存储菜单配置
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DictModel(Base):
    """字典表"""
    __tablename__ = "dicts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dict_type = Column(String(50), index=True, nullable=False)  # 字典类型
    label = Column(String(100), nullable=False)  # 显示标签
    value = Column(String(100), nullable=False)  # 字典值
    sort = Column(Integer, default=0)
    status = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DepartmentModel(Base):
    """部门表"""
    __tablename__ = "departments"

    id = Column(String(50), primary_key=True)
    department_name = Column(String(100), nullable=False)
    parent_id = Column(String(50), ForeignKey("departments.id"), nullable=True)
    status = Column(Integer, default=1)
    remark = Column(String(255), nullable=True)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # 自关联
    children = relationship("DepartmentModel", backref="parent", remote_side=[id])


class DepartmentUserModel(Base):
    """部门用户关联表"""
    __tablename__ = "department_users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    department_id = Column(String(50), ForeignKey("departments.id"), nullable=False)
    username = Column(String(50), nullable=False)
    account = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    status = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ExampleModel(Base):
    """示例表格数据"""
    __tablename__ = "examples"

    id = Column(String(50), primary_key=True)
    author = Column(String(50), nullable=True)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    importance = Column(Integer, default=1)
    display_time = Column(String(50), nullable=True)
    pageviews = Column(Integer, default=0)
    image_uri = Column(String(255), nullable=True)
    video_uri = Column(String(255), nullable=True)
    parent_id = Column(String(50), ForeignKey("examples.id"), nullable=True)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # 自关联（用于树形数据）
    children = relationship("ExampleModel", backref="parent", remote_side=[id])


class CardModel(Base):
    """卡片数据"""
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    logo = Column(String(255), nullable=True)
    name = Column(String(100), nullable=False)
    desc = Column(Text, nullable=True)
    status = Column(Integer, default=1)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
