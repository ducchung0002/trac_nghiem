from pydantic import BaseModel, EmailStr, Field

class TeacherAccount(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)

class StudentAccount(BaseModel):
    name: str = Field(max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)