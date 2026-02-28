"""
Example/Table API - 表格列表、树形列表、卡片列表、保存、详情、删除
"""
import uuid
import random
from typing import List, Optional
from fastapi import APIRouter, Query
from app.models.schemas import BaseResponse, DeleteRequest, SaveTableRequest

router = APIRouter(prefix="/example", tags=["example"])

SUCCESS_CODE = 0


def to_any_string():
    """生成随机字符串 ID"""
    return str(uuid.uuid4())


# 基础内容
BASE_CONTENT = '<p>I am testing data, I am testing data.</p><p><img src="https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943"></p>'

# 生成随机标题
TITLE_WORDS = ['Vue', 'React', 'Angular', 'Node', 'TypeScript', 'JavaScript', 'Python', 'Java', 'Go', 'Rust', 
               '前端', '后端', '全栈', '架构', '设计', '开发', '测试', '部署', '运维', '优化']


def generate_random_title():
    """生成随机标题"""
    words = random.sample(TITLE_WORDS, random.randint(5, 10))
    return ' '.join(words)


def generate_random_author():
    """生成随机作者名"""
    authors = ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Tom', 'Lucy', 'Lily', 'David', 'Emma']
    return random.choice(authors)


# 初始化表格数据
TABLE_LIST = []
for i in range(100):
    TABLE_LIST.append({
        "id": to_any_string(),
        "author": generate_random_author(),
        "title": generate_random_title(),
        "content": BASE_CONTENT,
        "importance": random.randint(1, 3),
        "display_time": "2024-01-01 12:00:00",
        "pageviews": random.randint(100, 500),
        "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}",
        "video_uri": "//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4"
    })


# 树形表格数据
TREE_LIST = []
for i in range(100):
    TREE_LIST.append({
        "id": to_any_string(),
        "author": generate_random_author(),
        "title": generate_random_title(),
        "content": BASE_CONTENT,
        "importance": random.randint(1, 3),
        "display_time": "2024-01-01 12:00:00",
        "pageviews": random.randint(300, 5000),
        "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}",
        "children": [
            {
                "id": to_any_string(),
                "author": generate_random_author(),
                "title": generate_random_title(),
                "content": BASE_CONTENT,
                "importance": random.randint(1, 3),
                "display_time": "2024-01-01 12:00:00",
                "pageviews": random.randint(300, 5000),
                "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}",
                "children": [
                    {
                        "id": to_any_string(),
                        "author": generate_random_author(),
                        "title": generate_random_title(),
                        "content": BASE_CONTENT,
                        "importance": random.randint(1, 3),
                        "display_time": "2024-01-01 12:00:00",
                        "pageviews": random.randint(300, 5000),
                        "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}"
                    },
                    {
                        "id": to_any_string(),
                        "author": generate_random_author(),
                        "title": generate_random_title(),
                        "content": BASE_CONTENT,
                        "importance": random.randint(1, 3),
                        "display_time": "2024-01-01 12:00:00",
                        "pageviews": random.randint(300, 5000),
                        "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}"
                    }
                ]
            },
            {
                "id": to_any_string(),
                "author": generate_random_author(),
                "title": generate_random_title(),
                "content": BASE_CONTENT,
                "importance": random.randint(1, 3),
                "display_time": "2024-01-01 12:00:00",
                "pageviews": random.randint(300, 5000),
                "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}"
            },
            {
                "id": to_any_string(),
                "author": generate_random_author(),
                "title": generate_random_title(),
                "content": BASE_CONTENT,
                "importance": random.randint(1, 3),
                "display_time": "2024-01-01 12:00:00",
                "pageviews": random.randint(300, 5000),
                "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}"
            },
            {
                "id": to_any_string(),
                "author": generate_random_author(),
                "title": generate_random_title(),
                "content": BASE_CONTENT,
                "importance": random.randint(1, 3),
                "display_time": "2024-01-01 12:00:00",
                "pageviews": random.randint(300, 5000),
                "image_uri": f"https://picsum.photos/{random.randint(100, 500)}x{random.randint(100, 500)}"
            }
        ]
    })


# 卡片列表数据
CARD_LIST = [
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "name": "Alipay",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png",
        "name": "Angular",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png",
        "name": "Bootstrap",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "name": "React",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png",
        "name": "Vue",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png",
        "name": "Webpack",
        "desc": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。"
    }
]


@router.get("/list", response_model=BaseResponse)
async def get_table_list(
    title: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10)
):
    """获取表格列表"""
    mock_list = TABLE_LIST
    if title:
        mock_list = [item for item in mock_list if title in item["title"]]
    
    start = (pageIndex - 1) * pageSize
    end = pageIndex * pageSize
    page_list = mock_list[start:end]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": len(mock_list),
            "list": page_list
        }
    )


@router.get("/treeList", response_model=BaseResponse)
async def get_tree_table_list(
    title: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10)
):
    """获取树形表格列表"""
    mock_list = TREE_LIST
    if title:
        mock_list = [item for item in mock_list if title in item["title"]]
    
    start = (pageIndex - 1) * pageSize
    end = pageIndex * pageSize
    page_list = mock_list[start:end]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": len(mock_list),
            "list": page_list
        }
    )


@router.get("/detail", response_model=BaseResponse)
async def get_table_detail(id: str = Query(...)):
    """获取表格详情"""
    for item in TABLE_LIST:
        if item["id"] == id:
            return BaseResponse(
                code=SUCCESS_CODE,
                data=item
            )
    return BaseResponse(
        code=404,
        message="数据不存在"
    )


@router.post("/save", response_model=BaseResponse)
async def save_table(data: SaveTableRequest):
    """保存表格数据"""
    if not data.id:
        # 新增
        new_item = {
            "id": to_any_string(),
            "author": data.author or generate_random_author(),
            "title": data.title or generate_random_title(),
            "content": data.content or BASE_CONTENT,
            "importance": data.importance or 1,
            "display_time": data.display_time or "2024-01-01 12:00:00",
            "pageviews": data.pageviews or 0,
            "image_uri": data.image_uri or "",
            "video_uri": data.video_uri or ""
        }
        TABLE_LIST.insert(0, new_item)
    else:
        # 更新
        for item in TABLE_LIST:
            if item["id"] == data.id:
                if data.author:
                    item["author"] = data.author
                if data.title:
                    item["title"] = data.title
                if data.content:
                    item["content"] = data.content
                if data.importance:
                    item["importance"] = data.importance
                if data.display_time:
                    item["display_time"] = data.display_time
                if data.pageviews:
                    item["pageviews"] = data.pageviews
                if data.image_uri:
                    item["image_uri"] = data.image_uri
                if data.video_uri:
                    item["video_uri"] = data.video_uri
                break
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


@router.post("/delete", response_model=BaseResponse)
async def delete_table(data: DeleteRequest):
    """删除表格数据"""
    if not data.ids:
        return BaseResponse(
            code=500,
            message="请选择需要删除的数据"
        )
    
    global TABLE_LIST
    TABLE_LIST = [item for item in TABLE_LIST if item["id"] not in data.ids]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data="success"
    )


# 卡片列表路由（单独的 /card 前缀）
card_router = APIRouter(prefix="/card", tags=["card"])


@card_router.get("/list", response_model=BaseResponse)
async def get_card_list(
    name: Optional[str] = Query(None),
    pageIndex: int = Query(1),
    pageSize: int = Query(10)
):
    """获取卡片列表"""
    mock_list = CARD_LIST
    if name:
        mock_list = [item for item in mock_list if name in item["name"]]
    
    start = (pageIndex - 1) * pageSize
    end = pageIndex * pageSize
    page_list = mock_list[start:end]
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "total": len(mock_list),
            "list": page_list
        }
    )
