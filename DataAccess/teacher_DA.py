from . import get_database
from Model import Teacher


class teacher_DA:
    def get_teacher_by_email(self, email: str) -> Teacher | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [teacher] WHERE [email]=%s", (email,))
            row = cursor.fetchone()
            if row is not None:
                return Teacher(row)
            return None

    def get_teacher_by_id(self, id: str) -> Teacher | None:
        with get_database(True) as cursor:
            cursor.execute("SELECT * FROM [teacher] WHERE [id]=%s", (id,))
            row = cursor.fetchone()
            if row is not None:
                return Teacher(row)
            return None

    def insert_teacher(self, email: str, hash_pswd: str, name: str):
        with get_database(True) as cursor:
            cursor.execute("INSERT INTO [teacher]([email], [hash_pswd], [name])  VALUES (%s, %s, %s)", (email, hash_pswd, name))

