from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from Model import Teacher
from Business.authenticate_bussiness import get_current_user
from typing import Annotated
from Business.student_business import student_bussiness
from .request_body_model import StudentAccount

student_router = APIRouter(prefix='/student', tags=['student'])


@student_router.get('/', status_code=status.HTTP_200_OK)
async def test(student: Annotated[Teacher, Depends(get_current_user)]):
    if student is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    return "Hello student: " + student.name


@student_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[StudentAccount, Body()], student_service: Annotated[student_bussiness, Depends()]):
    try:
        student_service.sign_up(email=data.email, password=data.password, name=data.name)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email is already existed!")

