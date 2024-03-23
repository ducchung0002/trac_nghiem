from Model import Teacher
from DataAccess.teacher_DA import teacher_DA
from . import bcrypt_context


class teacher_bussiness:
    def __init__(self):
        self.teacher_DA = teacher_DA()

    def authenticate(self, username, password) -> Teacher | None:
        teacher = self.teacher_DA.get_teacher_by_email(email=username)
        if teacher:
            if bcrypt_context.verify(password, teacher.hash_pswd):
                return teacher

        return None

    def authenticate_token(self, token: dict) -> Teacher | None:
        teacher = self.teacher_DA.get_teacher_by_id(id=token.get("id"))
        if teacher:
            if token.get("hash_pswd") == teacher.hash_pswd:
                return teacher

        return None

    def sign_up(self, email: str, password: str, name: str):
        self.teacher_DA.insert_teacher(email=email, hash_pswd=bcrypt_context.hash(password), name=name)