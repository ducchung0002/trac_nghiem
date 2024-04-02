from pydantic import BaseModel, EmailStr, Field


class Req_Teacher(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)


class Req_Student(BaseModel):
    id: str | None = None
    name: str = Field(max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)


class Req_Collection(BaseModel):
    teacher_id: str = Field(min_length=8, max_length=8)
    name: str = Field(max_length=100)


class Req_Collection(BaseModel):
    name: str
