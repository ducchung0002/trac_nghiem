from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from Model.db_model import Teacher
from Business.authenticate_bussiness import get_current_user
from typing import Annotated
from Business.student_business import student_bussiness
from Model.request_model import Req_Student
from Model.response_model import Res_Student

student_router = APIRouter(prefix='/student', tags=['student'])


@student_router.get('/', status_code=status.HTTP_200_OK)
async def get_student(student: Annotated[Teacher, Depends(get_current_user)]):
    if student is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    return Res_Student(**student_bussiness().get_student_by_id(student.id).__dict__)


@student_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Student, Body()], student_service: Annotated[student_bussiness, Depends()]):
    try:
        student_service.sign_up(data=data)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email is already existed!")
