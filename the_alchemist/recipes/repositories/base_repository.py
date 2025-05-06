from abc import ABC, abstractmethod
from recipes.models.base_recipe import BaseRecipe


class BaseRecipeRepository(ABC):
    model: BaseRecipe

    @abstractmethod
    def get_by_name(self, name: str) -> BaseRecipe:
        """Retrieve a recipe by its name."""
        raise NotImplementedError

    @abstractmethod
    def add(self, instance: BaseRecipe) -> None:
        """Add a new recipe."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[BaseRecipe]:
        """Retrieve all recipes."""
        raise NotImplementedError