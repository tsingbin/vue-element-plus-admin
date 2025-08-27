from flask import Blueprint, request, jsonify
import random
from datetime import datetime
import uuid

table_bp = Blueprint('table', __name__)

# ---- Mock Data ----

SUCCESS_CODE = 200

# ---- Helper Functions ----
def generate_id():
    return str(uuid.uuid4())

def random_title():
    words = ["Flask", "API", "Mock", "Example", "Data", "Test", "Random"]
    return " ".join(random.sample(words, random.randint(3, 6)))

def random_author():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    return random.choice(names)

def random_image():
    w = random.randint(100, 500)
    h = random.randint(100, 500)
    return f"https://via.placeholder.com/{w}x{h}"

base_content = "<p>I am testing data, I am testing data.</p><p><img src='https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943'></p>"

# ---- Generate Mock Lists ----
count = 100
List = [{
    "id": generate_id(),
    "author": random_author(),
    "title": random_title(),
    "content": base_content,
    "importance": random.randint(1, 3),
    "display_time": datetime.now().isoformat(),
    "pageviews": random.randint(100, 500),
    "image_uri": random_image(),
    "video_uri": "//sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-720p.mp4"
} for _ in range(count)]

treeList = [{
    "id": generate_id(),
    "author": random_author(),
    "title": random_title(),
    "content": base_content,
    "importance": random.randint(1, 3),
    "display_time": datetime.now().isoformat(),
    "pageviews": random.randint(300, 5000),
    "image_uri": random_image(),
    "children": [
        {
            "id": generate_id(),
            "author": random_author(),
            "title": random_title(),
            "content": base_content,
            "importance": random.randint(1, 3),
            "display_time": datetime.now().isoformat(),
            "pageviews": random.randint(300, 5000),
            "image_uri": random_image()
        }
    ]
} for _ in range(count)]

cardList = [
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "name": "Alipay",
        "desc": "中台产品研发过程中，设计规范和组件抽离的标准化示例。"
    },
    {
        "logo": "https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png",
        "name": "React",
        "desc": "在中台产品的研发过程中，设计与实现的差异会被统一标准化。"
    }
]

# ---- API Endpoints ----

# 树形列表接口
@table_bp.route('example/treeList', methods=['GET'])
def tree_list():
    title = request.args.get('title', '')
    page_index = int(request.args.get('pageIndex', 1))
    page_size = int(request.args.get('pageSize', 10))

    filtered = [item for item in treeList if title in item["title"]]
    start, end = (page_index - 1) * page_size, page_index * page_size
    page_list = filtered[start:end]

    return jsonify({"code": SUCCESS_CODE, "data": {"total": len(filtered), "list": page_list}})

# 列表接口
@table_bp.route('example/list', methods=['GET'])
def example_list():
    title = request.args.get('title', '')
    page_index = int(request.args.get('pageIndex', 1))
    page_size = int(request.args.get('pageSize', 10))

    filtered = [item for item in List if title in item["title"]]
    start, end = (page_index - 1) * page_size, page_index * page_size
    page_list = filtered[start:end]

    return jsonify({"code": SUCCESS_CODE, "data": {"total": len(filtered), "list": page_list}})

# 保存接口
@table_bp.route('example/save', methods=['POST'])
def save():
    data = request.get_json()
    if not data.get("id"):  # 新增
        new_item = {**data, "id": generate_id()}
        List.insert(0, new_item)
    else:  # 更新
        for item in List:
            if item["id"] == data["id"]:
                item.update(data)
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

# 详情接口
@table_bp.route('example/detail', methods=['GET'])
def detail():
    item_id = request.args.get("id")
    for item in List:
        if item["id"] == item_id:
            return jsonify({"code": SUCCESS_CODE, "data": item})
    return jsonify({"code": 404, "message": "Not found"}), 404

# 删除接口
@table_bp.route('example/delete', methods=['POST'])
def delete():
    data = request.get_json()
    ids = data.get("ids", [])
    if not ids:
        return jsonify({"code": 500, "message": "请选择需要删除的数据"}), 400
    global List
    List = [item for item in List if item["id"] not in ids]
    return jsonify({"code": SUCCESS_CODE, "data": "success"})

# 卡片列表接口
@table_bp.route('card/list', methods=['GET'])
def card_list():
    name = request.args.get('name', '')
    page_index = int(request.args.get('pageIndex', 1))
    page_size = int(request.args.get('pageSize', 10))

    filtered = [item for item in cardList if name in item["name"]]
    start, end = (page_index - 1) * page_size, page_index * page_size
    page_list = filtered[start:end]

    return jsonify({"code": SUCCESS_CODE, "data": {"total": len(filtered), "list": page_list}})
