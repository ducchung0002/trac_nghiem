from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class RM_Teacher(BaseModel):
    id: str
    email: str
    name: str
    avatar_path: str | None
    is_banned: bool


class RM_Student(BaseModel):
    id: str
    email: str
    name: str
    avatar_path: str | None
    is_banned: bool
