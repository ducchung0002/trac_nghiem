from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from Model import Teacher
from Business.authenticate_bussiness import get_current_user
from typing import Annotated
from Business.teacher_business import teacher_bussiness
from .request_body_model import TeacherAccount
from .response_model import RM_Teacher

teacher_router = APIRouter(prefix='/teacher', tags=['teacher'])


@teacher_router.get('/', status_code=status.HTTP_200_OK)
async def get_teacher(teacher: Annotated[Teacher, Depends(get_current_user)]):
    if teacher is None or not isinstance(teacher, Teacher):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    return RM_Teacher(**teacher_bussiness().get_teacher_by_id(teacher.id).__dict__)


@teacher_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[TeacherAccount, Body()], teacher_service: Annotated[teacher_bussiness, Depends()]):
    try:
        teacher_service.sign_up(email=data.email, password=data.password, name=data.name)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email is already existed!")
