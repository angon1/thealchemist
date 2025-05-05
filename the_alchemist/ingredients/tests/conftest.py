import pytest
from ingredients.factory.ingredient_factory import IngredientFactory
from ingredients.repositories.herb_json_repository import HerbJsonRepository
from ingredients.service import IngredientService
from ingredients.db.mappings import registered_ingredients


@pytest.fixture
def herb_repository():
    return HerbJsonRepository()


@pytest.fixture
def ingredient_factory():
    return IngredientFactory(registered_ingredients=registered_ingredients)


@pytest.fixture
def ingredient_service(herb_repository, ingredient_factory):
    return IngredientService(
        ingredient_repository=herb_repository, ingredient_factory=ingredient_factory
    )
