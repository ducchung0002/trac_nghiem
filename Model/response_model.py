from datetime import datetime

from pydantic import BaseModel


class Res_Token(BaseModel):
    access_token: str
    token_type: str


class Res_Student(BaseModel):
    id: str
    email: str
    name: str | None
    avatar_path: str | None
    is_banned: bool | None
    created_timestamp: datetime | None
    is_verified: bool | None


class Res_Teacher(BaseModel):
    id: str
    email: str
    name: str | None
    avatar_path: str | None
    is_banned: bool | None
    created_timestamp: datetime | None
    is_verified: bool | None


class Res_Collection(BaseModel):
    id: str
    teacher_id: str
    name: str | None
    created_timestamp: datetime | None
