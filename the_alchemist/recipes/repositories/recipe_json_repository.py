from pathlib import Path
from the_alchemist.settings import settings
from .base_json_recipe_repository import BaseJsonRecipeRepository
from recipes.models.base_recipe import BaseRecipe
from recipes.db.mappings import registered_recipe_types


class RecipeJsonRepository(BaseJsonRecipeRepository):
    def __init__(self, file_path: str = None):
        if file_path is None:
            final_path = Path(settings.DEFAULT_JSON_DB_PATH).resolve()
        else:
            final_path = Path(file_path).resolve()
        
        super().__init__(final_path)

    def get_by_name(self, name: str) -> BaseRecipe:
        data = self.data.get(name)
        if data:
            recipe_type = data.get("recipe_type")
            return registered_recipe_types[recipe_type](**data)
        return None

    def get_all(self) -> list[BaseRecipe]:
        return [
            registered_recipe_types[data["recipe_type"]](**data)
            for data in self.data.values()
        ]