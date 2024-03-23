class Admin:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.username = data.get("username")
        self.hash_pswd = data.get("hash_pswd")
        self.name = data.get("name")
        self.is_banned = data.get("is_banned")

class Student:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.email = data.get("email")
        self.hash_pswd = data.get("hash_pswd")
        self.name = data.get("name")
        self.avatar_path = data.get("avatar_path")
        self.is_banned = data.get("is_banned")

class Teacher:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.email = data.get("email")
        self.hash_pswd = data.get("hash_pswd")
        self.name = data.get("name")
        self.avatar_path = data.get("avatar_path")
        self.is_banned = data.get("is_banned")

class Group:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.name = data.get("name")
        self.teacher_id = data.get("teacher_id")
        self.created_timestamp = data.get("created_timestamp")
        self.is_show = data.get("is_show")

class GroupStudent:
    def __init__(self, data: dict) -> None:
        self.group_id = data.get("group_id")
        self.student_id = data.get("student_id")
        self.is_join = data.get("is_join")

class GroupTest:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.group_id = data.get("group_id")
        self.test_path = data.get("test_path")
        self.start = data.get("start")
        self.end = data.get("end")
        self.created_timestamp = data.get("created_timestamp")

class Collection:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.teacher_id = data.get("teacher_id")
        self.name = data.get("name")

class QuestionBank:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.collection_id = data.get("collection_id")
        self.name = data.get("name")

class GenerateTest:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.collection_id = data.get("collection_id")
        self.name = data.get("name")

class ManualTest:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.collection_id = data.get("collection_id")
        self.name = data.get("name")