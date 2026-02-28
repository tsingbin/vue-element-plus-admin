# Vue Element Plus Admin Backend

基于 FastAPI 的后端 API 服务，使用 MySQL 数据库存储数据。

## 目录结构

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 应用入口
│   ├── api/                 # API 路由模块
│   │   ├── __init__.py
│   │   ├── user.py          # 用户接口（登录、登出、用户列表）
│   │   ├── menu.py          # 菜单接口
│   │   ├── role.py          # 角色接口
│   │   ├── dict.py          # 字典接口
│   │   ├── department.py    # 部门接口
│   │   ├── table.py         # 表格/示例接口
│   │   ├── request.py       # 测试请求接口
│   │   ├── analysis.py      # 分析页统计接口
│   │   └── workplace.py     # 工作台接口
│   ├── db/                  # 数据库模块
│   │   ├── __init__.py
│   │   ├── database.py      # 数据库连接配置
│   │   ├── models.py        # SQLAlchemy 数据模型
│   │   └── init_db.py       # 数据库初始化脚本
│   └── models/              # Pydantic 模型
│       ├── __init__.py
│       └── schemas.py
├── venv/                    # Python 虚拟环境
├── .env                     # 环境变量配置
├── .env.example             # 环境变量配置模板
├── run.py                   # 启动脚本
├── requirements.txt         # Python 依赖
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 配置数据库

复制环境变量配置文件并修改：

```bash
cp .env.example .env
```

编辑 `.env` 文件，配置 MySQL 连接信息：

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=vepa_admin
```

### 3. 创建数据库

```sql
CREATE DATABASE vepa_admin CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. 初始化数据库（可选）

如果想手动初始化数据库表和种子数据：

```bash
cd backend
python -m app.db.init_db
```

或者直接启动服务，应用会自动创建表结构并初始化数据。

### 5. 启动服务

```bash
# 方式一：使用启动脚本（支持热重载）
python run.py

# 方式二：使用 uvicorn 直接启动
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

服务启动后访问：

- API 服务：http://127.0.0.1:8000
- API 文档（Swagger）：http://127.0.0.1:8000/docs
- API 文档（ReDoc）：http://127.0.0.1:8000/redoc

## API 接口列表

| 模块   | 路径                                   | 说明           |
| ------ | -------------------------------------- | -------------- |
| 用户   | `POST /api/user/login`                 | 用户登录       |
| 用户   | `GET /api/user/loginOut`               | 用户登出       |
| 用户   | `GET /api/user/list`                   | 用户列表       |
| 菜单   | `GET /api/menu/list`                   | 菜单列表       |
| 角色   | `GET /api/role/list`                   | 角色菜单列表   |
| 角色   | `GET /api/role/list2`                  | 角色权限路径   |
| 角色   | `GET /api/role/table`                  | 角色表格数据   |
| 字典   | `GET /api/dict/list`                   | 字典列表       |
| 字典   | `GET /api/dict/one`                    | 单个字典       |
| 部门   | `GET /api/department/list`             | 部门列表       |
| 部门   | `GET /api/department/table/list`       | 部门表格       |
| 部门   | `GET /api/department/users`            | 部门用户       |
| 部门   | `POST /api/department/user/save`       | 保存用户       |
| 部门   | `POST /api/department/user/delete`     | 删除用户       |
| 部门   | `POST /api/department/save`            | 保存部门       |
| 部门   | `POST /api/department/delete`          | 删除部门       |
| 表格   | `GET /api/example/list`                | 表格列表       |
| 表格   | `GET /api/example/treeList`            | 树形表格       |
| 表格   | `GET /api/example/detail`              | 表格详情       |
| 表格   | `POST /api/example/save`               | 保存表格       |
| 表格   | `POST /api/example/delete`             | 删除表格       |
| 卡片   | `GET /api/card/list`                   | 卡片列表       |
| 请求   | `GET /api/request/1-5`                 | 测试请求       |
| 请求   | `GET /api/request/expired`             | Token 过期测试 |
| 分析   | `GET /api/analysis/total`              | 统计数据       |
| 分析   | `GET /api/analysis/userAccessSource`   | 用户来源       |
| 分析   | `GET /api/analysis/weeklyUserActivity` | 周活跃量       |
| 分析   | `GET /api/analysis/monthlySales`       | 月销售额       |
| 工作台 | `GET /api/workplace/total`             | 统计数据       |
| 工作台 | `GET /api/workplace/project`           | 项目列表       |
| 工作台 | `GET /api/workplace/dynamic`           | 动态数据       |
| 工作台 | `GET /api/workplace/team`              | 团队信息       |
| 工作台 | `GET /api/workplace/radar`             | 指数数据       |

## 数据库表结构

| 表名             | 说明                   |
| ---------------- | ---------------------- |
| users            | 用户表                 |
| menus            | 菜单表（支持树形结构） |
| roles            | 角色表                 |
| dicts            | 字典表                 |
| departments      | 部门表（支持树形结构） |
| department_users | 部门用户表             |
| examples         | 示例表格数据           |
| cards            | 卡片数据               |

## 测试账号

| 用户名 | 密码  | 角色  | 权限               |
| ------ | ----- | ----- | ------------------ |
| admin  | admin | admin | 全部权限 (`*.*.*`) |
| test   | test  | test  | 有限权限           |

## 技术栈

- **FastAPI** - 现代、快速的 Web 框架
- **SQLAlchemy** - ORM 数据库工具
- **PyMySQL** - MySQL 数据库驱动
- **Uvicorn** - ASGI 服务器
- **Pydantic** - 数据验证

## 完整使用流程

```bash
# 1. 进入 backend 目录
cd backend

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置数据库连接（复制并修改 .env 文件）
cp .env.example .env
# 编辑 .env，填入你的 MySQL 配置：
# MYSQL_HOST=localhost
# MYSQL_PORT=3306
# MYSQL_USER=root
# MYSQL_PASSWORD=your_password
# MYSQL_DATABASE=vepa_admin

# 4. 创建数据库
mysql -u root -p -e "CREATE DATABASE vepa_admin CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. 启动服务（首次启动会自动创建表和初始化种子数据）
python run.py

# 服务启动后可访问：
# - API 服务：http://127.0.0.1:8000
# - Swagger 文档：http://127.0.0.1:8000/docs
# - ReDoc 文档：http://127.0.0.1:8000/redoc
```

### 测试接口

```bash
# 健康检查
curl http://127.0.0.1:8000/health

# 测试登录接口
curl -X POST http://127.0.0.1:8000/api/user/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}'

# 测试分析页统计
curl http://127.0.0.1:8000/api/analysis/total
```
