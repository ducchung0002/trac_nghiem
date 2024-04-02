from Model.db_model import Student
from Model.request_model import Req_Student
from DataAccess.student_DA import student_DA
from . import bcrypt_context


class student_bussiness:
    def __init__(self):
        self.student_DA = student_DA()

    def authenticate(self, username: str, password: str) -> Student | None:
        student = self.student_DA.get_student_by_email(email=username)
        if student:
            if bcrypt_context.verify(password, student.hash_pswd):
                return student
        return None

    # query
    def get_student_by_id(self, id: str) -> Student | None:
        return self.student_DA.get_student_by_id(id=id)

    # insert
    def sign_up(self, data: Req_Student) -> None:
        self.student_DA.insert_student(email=data.email, hash_pswd=bcrypt_context.hash(data.password), name=data.name)

    # update
    # delete
