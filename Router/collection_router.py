from fastapi import APIRouter, HTTPException, Depends, Body
from Model.request_model import Req_Collection
from Model.response_model import Res_Collection
from starlette import status
from typing import Annotated
from Model.db_model import Teacher
from Business.collection_business import collection_business
from Business.authenticate_bussiness import get_current_user
collection_router = APIRouter(prefix='/collection', tags=['collection'])



@collection_router.get('/', status_code=status.HTTP_200_OK, response_model=list[Res_Collection])
async def get_collections(teacher: Annotated[Teacher, Depends(get_current_user)],
                          collection_service: Annotated[collection_business, Depends()]):
    try:
        return collection_service.get_collections_by_teacher(teacher_id=teacher.id)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can not get collections!")


@collection_router.post('/', status_code=status.HTTP_201_CREATED)
async def insert_collection(teacher: Annotated[Teacher, Depends(get_current_user)],
                            data: Annotated[Req_Collection, Body()],
                            collection_service: Annotated[collection_business, Depends()]):
    try:
        collection_service.insert_collection(teacher_id=teacher.id, data=data)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Can not get collections!")