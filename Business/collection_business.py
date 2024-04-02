from Model.response_model import Res_Collection
from DataAccess.collection_DA import collection_DA
from Model.request_model import Req_Collection


class collection_business:
    def __init__(self):
        self.collection_DA = collection_DA()

    def get_collections_by_teacher(self, teacher_id: str) -> list[Res_Collection]:
        return [Res_Collection(**vars(collection)) for collection in
                self.collection_DA.get_collections_by_teacher(teacher_id=teacher_id)]

    def insert_collection(self, teacher_id: str, data: Req_Collection):
        self.collection_DA.insert_collection(teacher_id=teacher_id, name=data.name)
