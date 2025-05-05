from ..models.herb import Herb
from .json_repository import JsonRepository
from settings import settings
from pathlib import Path
class HerbJsonRepository(JsonRepository):
    model = Herb

    def __init__(self, file_path: str = None):
        if file_path is None:
            final_path = Path(settings.DEFAULT_JSON_DB_PATH).resolve()
        else:
            final_path = Path(file_path).resolve()
        
        super().__init__(final_path)

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
