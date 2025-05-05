from .ingredients.db.mappings import registered_ingredients
from .ingredients.factory.ingredient_factory import IngredientFactory
from .ingredients.repositories.herb_json_repository import HerbJsonRepository
from .ingredients.service import IngredientService


def create_service():
    """
    Create an instance of IngredientService with the necessary dependencies.
    """
    herb_repository = HerbJsonRepository()
    ingredient_factory = IngredientFactory(
        registered_ingredients=registered_ingredients
    )
    return IngredientService(
        ingredient_repository=herb_repository, ingredient_factory=ingredient_factory
    )


ingredient_app = create_service()
