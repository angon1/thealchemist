from ingredients.models.herb import Herb
from ingredients.repositories.json_repository import JsonRepository


class HerbJsonRepository(JsonRepository):
    model = Herb

    def __init__(self, file_path: str = "ingredients/db/herbs.json"):
        super().__init__(file_path)

    def get_by_name(self, name: str) -> Herb:
        """
        Get a herb by its name.
        """
        data = self.data.get(name)
        if data:
            return self.model(**data)
        return None

    def get_all(self) -> list[Herb]:
        """
        Get all herbs.
        """
        return [self.model(**data) for data in self.data.values()]
