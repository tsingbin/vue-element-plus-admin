# Vue Element Plus Admin Backend

基于 FastAPI 的后端 API 服务。

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
│   └── models/              # 数据模型
│       ├── __init__.py
│       └── schemas.py       # Pydantic 模型定义
├── venv/                    # Python 虚拟环境
├── run.py                   # 启动脚本
├── requirements.txt         # Python 依赖
└── README.md
```

## API 接口列表

| 模块   | 路径                               | 说明           |
| ------ | ---------------------------------- | -------------- |
| 用户   | `/api/user/login`                  | 用户登录       |
| 用户   | `/api/user/loginOut`               | 用户登出       |
| 用户   | `/api/user/list`                   | 用户列表       |
| 菜单   | `/api/menu/list`                   | 菜单列表       |
| 角色   | `/api/role/list`                   | 角色菜单列表   |
| 角色   | `/api/role/list2`                  | 角色权限路径   |
| 角色   | `/api/role/table`                  | 角色表格数据   |
| 字典   | `/api/dict/list`                   | 字典列表       |
| 字典   | `/api/dict/one`                    | 单个字典       |
| 部门   | `/api/department/list`             | 部门列表       |
| 部门   | `/api/department/table/list`       | 部门表格       |
| 部门   | `/api/department/users`            | 部门用户       |
| 部门   | `/api/department/user/save`        | 保存用户       |
| 部门   | `/api/department/user/delete`      | 删除用户       |
| 部门   | `/api/department/save`             | 保存部门       |
| 部门   | `/api/department/delete`           | 删除部门       |
| 表格   | `/api/example/list`                | 表格列表       |
| 表格   | `/api/example/treeList`            | 树形表格       |
| 表格   | `/api/example/detail`              | 表格详情       |
| 表格   | `/api/example/save`                | 保存表格       |
| 表格   | `/api/example/delete`              | 删除表格       |
| 卡片   | `/api/card/list`                   | 卡片列表       |
| 请求   | `/api/request/1-5`                 | 测试请求       |
| 请求   | `/api/request/expired`             | Token 过期测试 |
| 分析   | `/api/analysis/total`              | 统计数据       |
| 分析   | `/api/analysis/userAccessSource`   | 用户来源       |
| 分析   | `/api/analysis/weeklyUserActivity` | 周活跃量       |
| 分析   | `/api/analysis/monthlySales`       | 月销售额       |
| 工作台 | `/api/workplace/total`             | 统计数据       |
| 工作台 | `/api/workplace/project`           | 项目列表       |
| 工作台 | `/api/workplace/dynamic`           | 动态数据       |
| 工作台 | `/api/workplace/team`              | 团队信息       |
| 工作台 | `/api/workplace/radar`             | 指数数据       |

## 快速开始

### 1. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 启动服务

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

### 3. 测试接口

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

## 测试账号

| 用户名 | 密码  | 角色  | 权限               |
| ------ | ----- | ----- | ------------------ |
| admin  | admin | admin | 全部权限 (`*.*.*`) |
| test   | test  | test  | 有限权限           |

## 技术栈

- **FastAPI** - 现代、快速的 Web 框架
- **Uvicorn** - ASGI 服务器
- **Pydantic** - 数据验证
