from . import get_database
from Model.db_model import Student


class student_DA:
    def get_student_by_email(self, email: str) -> Student | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [email]=%s", (email,))
            row = cursor.fetchone()
            if row is not None:
                return Student(row)
            return None

    def get_student_by_id(self, id: str) -> Student | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [student] WHERE [id]=%s", (id,))
            row = cursor.fetchone()
            if row is not None:
                return Student(row)
            return None

    def insert_student(self, email: str, hash_pswd: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [student]([email], [hash_pswd], [name])  VALUES (%s, %s, %s)", (email, hash_pswd, name))
