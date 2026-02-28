"""
Pydantic models for request/response validation
"""
from typing import Any, List, Optional
from pydantic import BaseModel


class BaseResponse(BaseModel):
    code: int = 0
    message: str = ""
    data: Any = None


class UserLogin(BaseModel):
    username: str
    password: str


class UserInfo(BaseModel):
    username: str
    password: str
    role: str
    roleId: str
    permissions: List[str]


class UserListResponse(BaseModel):
    total: int
    list: List[UserInfo]


class DeleteRequest(BaseModel):
    ids: List[str]


class SaveUserRequest(BaseModel):
    id: Optional[str] = None
    username: Optional[str] = None
    account: Optional[str] = None
    email: Optional[str] = None


class SaveDepartmentRequest(BaseModel):
    id: Optional[str] = None
    departmentName: Optional[str] = None
    status: Optional[int] = None
    remark: Optional[str] = None


class SaveTableRequest(BaseModel):
    id: Optional[str] = None
    author: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    importance: Optional[int] = None
    display_time: Optional[str] = None
    pageviews: Optional[int] = None
    image_uri: Optional[str] = None
    video_uri: Optional[str] = None
