"""
数据库初始化脚本 - 插入种子数据
"""
import json
import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base
from app.db.models import (
    UserModel, MenuModel, RoleModel, DictModel,
    DepartmentModel, DepartmentUserModel, ExampleModel, CardModel
)


def to_any_string():
    """生成随机字符串 ID"""
    return str(uuid.uuid4())


def init_users(db: Session):
    """初始化用户数据"""
    # 检查是否已有数据
    if db.query(UserModel).first():
        return
    
    users = [
        UserModel(
            username="admin",
            password="admin",
            role="admin",
            role_id="1",
            permissions=json.dumps(["*.*.*"]),
            status=1
        ),
        UserModel(
            username="test",
            password="test",
            role="test",
            role_id="2",
            permissions=json.dumps(["example:dialog:create", "example:dialog:delete"]),
            status=1
        )
    ]
    db.add_all(users)
    db.commit()
    print("✓ 用户数据初始化完成")


def init_menus(db: Session):
    """初始化菜单数据"""
    if db.query(MenuModel).first():
        return
    
    menus_data = [
        # Dashboard
        {"id": 1, "path": "/dashboard", "component": "#", "redirect": "/dashboard/analysis", "name": "Dashboard", "status": 1, "type": 0, "parent_id": None, "title": "首页", "icon": "vi-ant-design:dashboard-filled", "meta": {"title": "首页", "icon": "vi-ant-design:dashboard-filled", "alwaysShow": True}},
        {"id": 2, "path": "analysis", "component": "views/Dashboard/Analysis", "name": "Analysis", "status": 1, "type": 1, "parent_id": 1, "title": "分析页", "meta": {"title": "分析页", "noCache": True}},
        {"id": 3, "path": "workplace", "component": "views/Dashboard/Workplace", "name": "Workplace", "status": 1, "type": 1, "parent_id": 1, "title": "工作台", "meta": {"title": "工作台", "noCache": True}},
        # External Link
        {"id": 4, "path": "/external-link", "component": "#", "name": "ExternalLink", "status": 1, "type": 0, "parent_id": None, "title": "文档", "icon": "vi-clarity:document-solid", "meta": {"title": "文档", "icon": "vi-clarity:document-solid"}},
        {"id": 5, "path": "https://element-plus-admin-doc.cn/", "name": "DocumentLink", "status": 1, "type": 1, "parent_id": 4, "title": "文档", "meta": {"title": "文档"}},
        # Level
        {"id": 6, "path": "/level", "component": "#", "redirect": "/level/menu1/menu1-1/menu1-1-1", "name": "Level", "status": 1, "type": 0, "parent_id": None, "title": "菜单", "icon": "vi-carbon:skill-level-advanced", "meta": {"title": "菜单", "icon": "vi-carbon:skill-level-advanced"}},
        {"id": 7, "path": "menu1", "name": "Menu1", "component": "##", "status": 1, "type": 0, "parent_id": 6, "title": "菜单1", "redirect": "/level/menu1/menu1-1/menu1-1-1", "meta": {"title": "菜单1"}},
        {"id": 8, "path": "menu1-1", "name": "Menu11", "component": "##", "status": 1, "type": 0, "parent_id": 7, "title": "菜单1-1", "redirect": "/level/menu1/menu1-1/menu1-1-1", "meta": {"title": "菜单1-1", "alwaysShow": True}},
        {"id": 9, "path": "menu1-1-1", "name": "Menu111", "component": "views/Level/Menu111", "status": 1, "type": 1, "parent_id": 8, "title": "菜单1-1-1", "meta": {"title": "菜单1-1-1"}},
        {"id": 10, "path": "menu1-2", "name": "Menu12", "component": "views/Level/Menu12", "status": 1, "type": 1, "parent_id": 7, "title": "菜单1-2", "meta": {"title": "菜单1-2"}},
        {"id": 11, "path": "menu2", "name": "Menu2Demo", "component": "views/Level/Menu2", "status": 1, "type": 1, "parent_id": 6, "title": "菜单2", "meta": {"title": "菜单2"}},
        # Example
        {"id": 12, "path": "/example", "component": "#", "redirect": "/example/example-dialog", "name": "Example", "status": 1, "type": 0, "parent_id": None, "title": "综合示例", "icon": "vi-ep:management", "meta": {"title": "综合示例", "icon": "vi-ep:management", "alwaysShow": True}},
        {"id": 13, "path": "example-dialog", "component": "views/Example/Dialog/ExampleDialog", "name": "ExampleDialog", "status": 1, "type": 1, "parent_id": 12, "title": "综合示例-弹窗", "meta": {"title": "综合示例-弹窗"}},
        {"id": 14, "path": "example-page", "component": "views/Example/Page/ExamplePage", "name": "ExamplePage", "status": 1, "type": 1, "parent_id": 12, "title": "综合示例-页面", "meta": {"title": "综合示例-页面"}},
        {"id": 15, "path": "example-add", "component": "views/Example/Page/ExampleAdd", "name": "ExampleAdd", "status": 1, "type": 1, "parent_id": 12, "title": "综合示例-新增", "meta": {"title": "综合示例-新增", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}},
        {"id": 16, "path": "example-edit", "component": "views/Example/Page/ExampleEdit", "name": "ExampleEdit", "status": 1, "type": 1, "parent_id": 12, "title": "综合示例-编辑", "meta": {"title": "综合示例-编辑", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}},
        {"id": 17, "path": "example-detail", "component": "views/Example/Page/ExampleDetail", "name": "ExampleDetail", "status": 1, "type": 1, "parent_id": 12, "title": "综合示例-详情", "meta": {"title": "综合示例-详情", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}},
    ]
    
    for menu_data in menus_data:
        menu = MenuModel(**menu_data)
        db.add(menu)
    
    db.commit()
    print("✓ 菜单数据初始化完成")


def init_roles(db: Session):
    """初始化角色数据"""
    if db.query(RoleModel).first():
        return
    
    roles = [
        RoleModel(
            id=to_any_string(),
            role_name="超级管理员",
            role="admin",
            status=1,
            remark="拥有所有权限"
        ),
        RoleModel(
            id=to_any_string(),
            role_name="管理员",
            role="manager",
            status=1,
            remark="管理普通用户"
        ),
        RoleModel(
            id=to_any_string(),
            role_name="普通用户",
            role="user",
            status=1,
            remark="普通用户权限"
        ),
        RoleModel(
            id=to_any_string(),
            role_name="游客",
            role="guest",
            status=1,
            remark="只读权限"
        ),
    ]
    db.add_all(roles)
    db.commit()
    print("✓ 角色数据初始化完成")


def init_dicts(db: Session):
    """初始化字典数据"""
    if db.query(DictModel).first():
        return
    
    dicts = [
        DictModel(dict_type="importance", label="tableDemo.commonly", value="0", sort=0),
        DictModel(dict_type="importance", label="tableDemo.good", value="1", sort=1),
        DictModel(dict_type="importance", label="tableDemo.important", value="2", sort=2),
        DictModel(dict_type="test", label="test1", value="0", sort=0),
        DictModel(dict_type="test", label="test2", value="1", sort=1),
        DictModel(dict_type="test", label="test3", value="2", sort=2),
    ]
    db.add_all(dicts)
    db.commit()
    print("✓ 字典数据初始化完成")


def init_departments(db: Session):
    """初始化部门数据"""
    if db.query(DepartmentModel).first():
        return
    
    cities = ['厦门总公司', '北京分公司', '上海分公司', '福州分公司', '深圳分公司']
    depts = ['研发部', '产品部', '运营部', '市场部', '销售部', '客服部']
    
    for i, city in enumerate(cities):
        parent_id = to_any_string()
        parent = DepartmentModel(
            id=parent_id,
            department_name=city,
            status=1,
            remark=f"{city}备注"
        )
        db.add(parent)
        
        for dept in depts:
            child = DepartmentModel(
                id=to_any_string(),
                department_name=dept,
                parent_id=parent_id,
                status=1,
                remark=f"{city}-{dept}备注"
            )
            db.add(child)
    
    db.commit()
    print("✓ 部门数据初始化完成")


def init_examples(db: Session):
    """初始化示例数据"""
    if db.query(ExampleModel).first():
        return
    
    import random
    
    base_content = '<p>I am testing data, I am testing data.</p><p><img src="https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943"></p>'
    titles = ['Vue', 'React', 'Angular', 'Node', 'TypeScript', 'JavaScript', 'Python', 'Java', 'Go', 'Rust']
    authors = ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Tom', 'Lucy', 'Lily', 'David', 'Emma']
    
    for i in range(20):
        example = ExampleModel(
            id=to_any_string(),
            author=random.choice(authors),
            title=f"{random.choice(titles)} 教程 {i+1}",
            content=base_content,
            importance=random.randint(1, 3),
            display_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pageviews=random.randint(100, 500),
            image_uri=f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}",
            video_uri="//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4"
        )
        db.add(example)
    
    db.commit()
    print("✓ 示例数据初始化完成")


def init_cards(db: Session):
    """初始化卡片数据"""
    if db.query(CardModel).first():
        return
    
    cards = [
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png", name="Alipay", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png", name="Angular", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png", name="Bootstrap", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png", name="React", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png", name="Vue", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
        CardModel(logo="https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png", name="Webpack", desc="在中台产品的研发过程中，会出现不同的设计规范和实现方式。"),
    ]
    db.add_all(cards)
    db.commit()
    print("✓ 卡片数据初始化完成")


def init_database():
    """初始化数据库表结构和种子数据"""
    print("开始初始化数据库...")
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("✓ 数据库表创建完成")
    
    # 获取数据库会话
    db = SessionLocal()
    
    try:
        init_users(db)
        init_menus(db)
        init_roles(db)
        init_dicts(db)
        init_departments(db)
        init_examples(db)
        init_cards(db)
        print("\n✅ 数据库初始化完成！")
    except Exception as e:
        print(f"\n❌ 数据库初始化失败: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
