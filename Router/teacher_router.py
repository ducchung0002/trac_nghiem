from fastapi import APIRouter, HTTPException, Depends, Body
from starlette import status
from Model.db_model import Teacher
from Business.authenticate_bussiness import get_current_user
from typing import Annotated
from Business.teacher_business import teacher_bussiness
from Model.request_model import Req_Teacher
from Model.response_model import Res_Teacher
from .collection_router import collection_router

teacher_router = APIRouter(prefix='/teacher', tags=['teacher'])
teacher_router.include_router(collection_router)


@teacher_router.get('/', status_code=status.HTTP_200_OK)
async def get_teacher(teacher: Annotated[Teacher, Depends(get_current_user)]):
    if teacher is None or not isinstance(teacher, Teacher):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')

    return Res_Teacher.model_dump(teacher_bussiness().get_teacher_by_id(teacher.id))
    # return Res_Teacher(**vars(teacher_bussiness().get_teacher_by_id(teacher.id)))


@teacher_router.post('/sign_up', status_code=status.HTTP_201_CREATED)
async def sign_up(data: Annotated[Req_Teacher, Body()], teacher_service: Annotated[teacher_bussiness, Depends()]):
    try:
        teacher_service.sign_up(data)
    except:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email is already existed!")
