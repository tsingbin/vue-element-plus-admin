"""
Role API - 角色列表、角色表格
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import RoleModel, MenuModel
from app.models.schemas import BaseResponse

router = APIRouter(prefix="/role", tags=["role"])

SUCCESS_CODE = 0

# 管理员菜单列表（静态数据，用于 role/list 接口）
ADMIN_MENU_LIST = [
    {
        "path": "/dashboard",
        "component": "#",
        "redirect": "/dashboard/analysis",
        "name": "Dashboard",
        "meta": {"title": "router.dashboard", "icon": "vi-ant-design:dashboard-filled", "alwaysShow": True},
        "children": [
            {"path": "analysis", "component": "views/Dashboard/Analysis", "name": "Analysis", "meta": {"title": "router.analysis", "noCache": True, "affix": True}},
            {"path": "workplace", "component": "views/Dashboard/Workplace", "name": "Workplace", "meta": {"title": "router.workplace", "noCache": True, "affix": True}}
        ]
    },
    {
        "path": "/external-link",
        "component": "#",
        "meta": {},
        "name": "ExternalLink",
        "children": [
            {"path": "https://element-plus-admin-doc.cn/", "name": "DocumentLink", "meta": {"title": "router.document", "icon": "vi-clarity:document-solid"}}
        ]
    },
    {
        "path": "/guide",
        "component": "#",
        "name": "Guide",
        "meta": {},
        "children": [
            {"path": "index", "component": "views/Guide/Guide", "name": "GuideDemo", "meta": {"title": "router.guide", "icon": "vi-cib:telegram-plane"}}
        ]
    },
    {
        "path": "/components",
        "component": "#",
        "redirect": "/components/form/default-form",
        "name": "ComponentsDemo",
        "meta": {"title": "router.component", "icon": "vi-bx:bxs-component", "alwaysShow": True},
        "children": [
            {
                "path": "form", "name": "Form", "component": "##", "meta": {"title": "router.form", "alwaysShow": True},
                "children": [
                    {"path": "default-form", "component": "views/Components/Form/DefaultForm", "name": "DefaultForm", "meta": {"title": "router.defaultForm"}},
                    {"path": "use-form", "component": "views/Components/Form/UseFormDemo", "name": "UseForm", "meta": {"title": "UseForm"}}
                ]
            },
            {
                "path": "table", "name": "TableDemo", "component": "##", "redirect": "/components/table/default-table", "meta": {"title": "router.table", "alwaysShow": True},
                "children": [
                    {"path": "default-table", "component": "views/Components/Table/DefaultTable", "name": "DefaultTable", "meta": {"title": "router.defaultTable"}},
                    {"path": "use-table", "component": "views/Components/Table/UseTableDemo", "name": "UseTable", "meta": {"title": "UseTable"}},
                    {"path": "tree-table", "component": "views/Components/Table/TreeTable", "name": "TreeTable", "meta": {"title": "router.treeTable"}},
                    {"path": "table-image-preview", "component": "views/Components/Table/TableImagePreview", "name": "TableImagePreview", "meta": {"title": "router.PicturePreview"}},
                    {"path": "table-video-preview", "component": "views/Components/Table/TableVideoPreview", "name": "TableVideoPreview", "meta": {"title": "router.tableVideoPreview"}},
                    {"path": "card-table", "component": "views/Components/Table/CardTable", "name": "CardTable", "meta": {"title": "router.cardTable"}}
                ]
            },
            {
                "path": "editor-demo", "name": "EditorDemo", "component": "##", "redirect": "/components/editor-demo/editor", "meta": {"title": "router.editor", "alwaysShow": True},
                "children": [
                    {"path": "editor", "component": "views/Components/Editor/Editor", "name": "Editor", "meta": {"title": "router.richText"}},
                    {"path": "json-editor", "component": "views/Components/Editor/JsonEditor", "name": "JsonEditor", "meta": {"title": "router.jsonEditor"}},
                    {"path": "code-editor", "component": "views/Components/Editor/CodeEditor", "name": "CodeEditor", "meta": {"title": "router.codeEditor"}}
                ]
            },
            {"path": "search", "component": "views/Components/Search", "name": "Search", "meta": {"title": "router.search"}},
            {"path": "descriptions", "component": "views/Components/Descriptions", "name": "Descriptions", "meta": {"title": "router.descriptions"}},
            {"path": "image-viewer", "component": "views/Components/ImageViewer", "name": "ImageViewer", "meta": {"title": "router.imageViewer"}},
            {"path": "dialog", "component": "views/Components/Dialog", "name": "Dialog", "meta": {"title": "router.dialog"}},
            {"path": "icon", "component": "views/Components/Icon", "name": "Icon", "meta": {"title": "router.icon"}},
            {"path": "icon-picker", "component": "views/Components/IconPicker", "name": "IconPicker", "meta": {"title": "router.iconPicker"}},
            {"path": "echart", "component": "views/Components/Echart", "name": "Echart", "meta": {"title": "router.echart"}},
            {"path": "count-to", "component": "views/Components/CountTo", "name": "CountTo", "meta": {"title": "router.countTo"}},
            {"path": "qrcode", "component": "views/Components/Qrcode", "name": "Qrcode", "meta": {"title": "router.qrcode"}},
            {"path": "highlight", "component": "views/Components/Highlight", "name": "Highlight", "meta": {"title": "router.highlight"}},
            {"path": "infotip", "component": "views/Components/Infotip", "name": "Infotip", "meta": {"title": "router.infotip"}},
            {"path": "input-password", "component": "views/Components/InputPassword", "name": "InputPassword", "meta": {"title": "router.inputPassword"}},
            {"path": "waterfall", "component": "views/Components/Waterfall", "name": "Waterfall", "meta": {"title": "router.waterfall"}},
            {"path": "image-cropping", "component": "views/Components/ImageCropping", "name": "ImageCropping", "meta": {"title": "router.imageCropping"}},
            {"path": "video-player", "component": "views/Components/VideoPlayer", "name": "VideoPlayer", "meta": {"title": "router.videoPlayer"}},
            {"path": "avatars", "component": "views/Components/Avatars", "name": "Avatars", "meta": {"title": "router.avatars"}},
            {"path": "i-agree", "component": "views/Components/IAgree", "name": "IAgree", "meta": {"title": "router.iAgree"}},
            {"path": "tree", "component": "views/Components/Tree", "name": "Tree", "meta": {"title": "router.tree"}}
        ]
    },
    {
        "path": "/function",
        "component": "#",
        "redirect": "/function/multipleTabs",
        "name": "Function",
        "meta": {"title": "router.function", "icon": "vi-ri:function-fill", "alwaysShow": True},
        "children": [
            {"path": "multiple-tabs", "component": "views/Function/MultipleTabs", "name": "MultipleTabs", "meta": {"title": "router.multipleTabs"}},
            {"path": "multiple-tabs-demo/:id", "component": "views/Function/MultipleTabsDemo", "name": "MultipleTabsDemo", "meta": {"hidden": True, "title": "router.details", "canTo": True, "activeMenu": "/function/multiple-tabs"}},
            {"path": "request", "component": "views/Function/Request", "name": "Request", "meta": {"title": "router.request"}},
            {"path": "test", "component": "views/Function/Test", "name": "Test", "meta": {"title": "router.permission", "permission": ["add", "edit", "delete"]}}
        ]
    },
    {
        "path": "/hooks",
        "component": "#",
        "redirect": "/hooks/useWatermark",
        "name": "Hooks",
        "meta": {"title": "hooks", "icon": "vi-ic:outline-webhook", "alwaysShow": True},
        "children": [
            {"path": "useWatermark", "component": "views/hooks/useWatermark", "name": "UseWatermark", "meta": {"title": "useWatermark"}},
            {"path": "useTagsView", "component": "views/hooks/useTagsView", "name": "UseTagsView", "meta": {"title": "useTagsView"}},
            {"path": "useValidator", "component": "views/hooks/useValidator", "name": "UseValidator", "meta": {"title": "useValidator"}},
            {"path": "useCrudSchemas", "component": "views/hooks/useCrudSchemas", "name": "UseCrudSchemas", "meta": {"title": "useCrudSchemas"}},
            {"path": "useClipboard", "component": "views/hooks/useClipboard", "name": "UseClipboard", "meta": {"title": "useClipboard"}},
            {"path": "useNetwork", "component": "views/hooks/useNetwork", "name": "UseNetwork", "meta": {"title": "useNetwork"}}
        ]
    },
    {
        "path": "/level",
        "component": "#",
        "redirect": "/level/menu1/menu1-1/menu1-1-1",
        "name": "Level",
        "meta": {"title": "router.level", "icon": "vi-carbon:skill-level-advanced"},
        "children": [
            {
                "path": "menu1", "name": "Menu1", "component": "##", "redirect": "/level/menu1/menu1-1/menu1-1-1", "meta": {"title": "router.menu1"},
                "children": [
                    {
                        "path": "menu1-1", "name": "Menu11", "component": "##", "redirect": "/level/menu1/menu1-1/menu1-1-1", "meta": {"title": "router.menu11", "alwaysShow": True},
                        "children": [
                            {"path": "menu1-1-1", "name": "Menu111", "component": "views/Level/Menu111", "meta": {"title": "router.menu111"}}
                        ]
                    },
                    {"path": "menu1-2", "name": "Menu12", "component": "views/Level/Menu12", "meta": {"title": "router.menu12"}}
                ]
            },
            {"path": "menu2", "name": "Menu2Demo", "component": "views/Level/Menu2", "meta": {"title": "router.menu2"}}
        ]
    },
    {
        "path": "/example",
        "component": "#",
        "redirect": "/example/example-dialog",
        "name": "Example",
        "meta": {"title": "router.example", "icon": "vi-ep:management", "alwaysShow": True},
        "children": [
            {"path": "example-dialog", "component": "views/Example/Dialog/ExampleDialog", "name": "ExampleDialog", "meta": {"title": "router.exampleDialog"}},
            {"path": "example-page", "component": "views/Example/Page/ExamplePage", "name": "ExamplePage", "meta": {"title": "router.examplePage"}},
            {"path": "example-add", "component": "views/Example/Page/ExampleAdd", "name": "ExampleAdd", "meta": {"title": "router.exampleAdd", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}},
            {"path": "example-edit", "component": "views/Example/Page/ExampleEdit", "name": "ExampleEdit", "meta": {"title": "router.exampleEdit", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}},
            {"path": "example-detail", "component": "views/Example/Page/ExampleDetail", "name": "ExampleDetail", "meta": {"title": "router.exampleDetail", "noTagsView": True, "noCache": True, "hidden": True, "showMainRoute": True, "activeMenu": "/example/example-page"}}
        ]
    },
    {
        "path": "/error",
        "component": "#",
        "redirect": "/error/404",
        "name": "Error",
        "meta": {"title": "router.errorPage", "icon": "vi-ci:error", "alwaysShow": True},
        "children": [
            {"path": "404-demo", "component": "views/Error/404", "name": "404Demo", "meta": {"title": "404"}},
            {"path": "403-demo", "component": "views/Error/403", "name": "403Demo", "meta": {"title": "403"}},
            {"path": "500-demo", "component": "views/Error/500", "name": "500Demo", "meta": {"title": "500"}}
        ]
    },
    {
        "path": "/authorization",
        "component": "#",
        "redirect": "/authorization/user",
        "name": "Authorization",
        "meta": {"title": "router.authorization", "icon": "vi-eos-icons:role-binding", "alwaysShow": True},
        "children": [
            {"path": "department", "component": "views/Authorization/Department/Department", "name": "Department", "meta": {"title": "router.department"}},
            {"path": "user", "component": "views/Authorization/User/User", "name": "User", "meta": {"title": "router.user"}},
            {"path": "menu", "component": "views/Authorization/Menu/Menu", "name": "Menu", "meta": {"title": "router.menuManagement"}},
            {"path": "role", "component": "views/Authorization/Role/Role", "name": "Role", "meta": {"title": "router.role"}}
        ]
    }
]

# 测试用户权限路径列表
TEST_LIST = [
    '/dashboard', '/dashboard/analysis', '/dashboard/workplace',
    'external-link', 'https://element-plus-admin-doc.cn/',
    '/level', '/level/menu1', '/level/menu1/menu1-1', '/level/menu1/menu1-1/menu1-1-1',
    '/level/menu1/menu1-2', '/level/menu2',
    '/example', '/example/example-dialog', '/example/example-page'
]


@router.get("/list", response_model=BaseResponse)
async def get_role_list(db: Session = Depends(get_db)):
    """获取角色列表（管理员菜单）"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=ADMIN_MENU_LIST
    )


@router.get("/list2", response_model=BaseResponse)
async def get_role_list2():
    """获取角色列表2（测试用户权限路径）"""
    return BaseResponse(
        code=SUCCESS_CODE,
        data=TEST_LIST
    )


@router.get("/table", response_model=BaseResponse)
async def get_role_table(db: Session = Depends(get_db)):
    """获取角色表格数据"""
    roles = db.query(RoleModel).all()
    
    role_list = []
    for role in roles:
        role_list.append({
            "id": role.id,
            "roleName": role.role_name,
            "role": role.role,
            "status": role.status,
            "createTime": role.create_time.strftime("%Y-%m-%d %H:%M:%S") if role.create_time else None,
            "remark": role.remark,
            "menu": role.menu or []
        })
    
    return BaseResponse(
        code=SUCCESS_CODE,
        data={
            "list": role_list,
            "total": len(role_list)
        }
    )