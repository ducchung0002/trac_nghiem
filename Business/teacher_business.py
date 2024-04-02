from Model.db_model import Teacher
from DataAccess.teacher_DA import teacher_DA
from . import bcrypt_context
from Model.request_model import Req_Teacher



class teacher_bussiness:
    def __init__(self):
        self.teacher_DA = teacher_DA()

    def authenticate(self, username: str, password: str) -> Teacher | None:
        teacher = self.teacher_DA.get_teacher_by_email(email=username)
        if teacher:
            if bcrypt_context.verify(password, teacher.hash_pswd):
                return teacher
        return None

    def get_teacher_by_id(self, id: str) -> Teacher | None:
        return self.teacher_DA.get_teacher_by_id(id=id)

    # insert
    def sign_up(self, data: Req_Teacher) -> None:
        self.teacher_DA.insert_teacher(email=data.email, hash_pswd=bcrypt_context.hash(data.password), name=data.name)

