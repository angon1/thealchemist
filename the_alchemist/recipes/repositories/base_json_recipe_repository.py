import json
from pathlib import Path
from .base_repository import BaseRecipeRepository
from recipes.models.base_recipe import BaseRecipe


class BaseJsonRecipeRepository(BaseRecipeRepository):
    def __init__(self, file_path: str):
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        self.file_path = Path(file_path).resolve()
        self.data = self.load_data()

    def load_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file)

    def add(self, instance: BaseRecipe):
        self.data[instance.product] = instance.to_dict()
        self.save_data()

    def get_by_name(self, name: str) -> BaseRecipe:
        raise NotImplementedError("This method must be implemented by subclasses.")

    def get_all(self) -> list[BaseRecipe]:
        raise NotImplementedError("This method must be implemented by subclasses.")