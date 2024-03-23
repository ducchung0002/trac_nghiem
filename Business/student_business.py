from Model import Student
from DataAccess.student_DA import student_DA
from . import bcrypt_context


class student_bussiness:
    def __init__(self):
        self.student_DA = student_DA()

    def authenticate(self, username, password) -> Student | None:
        student = self.student_DA.get_student_by_email(email=username)
        if student:
            if bcrypt_context.verify(password, student.hash_pswd):
                return student

        return None

    def authenticate_token(self, token):
        student = self.student_DA.get_student_by_id(id=token.get("id"))
        if student:
            if token.get("hash_pswd") == student.hash_pswd:
                return student

        return None

    def sign_up(self, email: str, password: str, name: str):
        self.student_DA.insert_student(email=email, hash_pswd=bcrypt_context.hash(password), name=name)