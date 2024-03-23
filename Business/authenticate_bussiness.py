import starlette.status
import typing
import fastapi
from jose import jwt, JWTError
from datetime import datetime, timedelta
from Business.teacher_business import teacher_bussiness
from Business.student_business import student_bussiness
from . import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, HASH_ALGORITHM, oauth2_scheme


def create_access_token(data: dict, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    encode = data.copy()
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=HASH_ALGORITHM)


async def get_current_user(token: typing.Annotated[str, fastapi.Depends(oauth2_scheme)]):
    credentials_exception = fastapi.HTTPException(
        status_code=starlette.status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        role = payload.get("role")
        if role == "teacher":
            teacher_service = teacher_bussiness()
            teacher = teacher_service.authenticate_token(payload)
            if teacher is None:
                raise credentials_exception
            return teacher
        elif role == "student":
            student_service = student_bussiness()
            student = student_service.authenticate_token(payload)
            if student is None:
                raise credentials_exception
            return student
        elif role == "admin":
            pass
        else:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
