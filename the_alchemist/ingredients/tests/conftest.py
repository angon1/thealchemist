import pytest
from ingredients.factory.ingredient_factory import IngredientFactory
from ingredients.repositories.herb_json_repository import HerbJsonRepository
from ingredients.service import IngredientService
from ingredients.db.mappings import registered_ingredients


@pytest.fixture
def herb_repository():
    """Fixture for creating a HerbJsonRepository instance.

    Returns:
        HerbJsonRepository: An instance of the herb repository.
    """
    return HerbJsonRepository()


@pytest.fixture
def ingredient_factory():
    """Fixture for creating an IngredientFactory instance.

    Returns:
        IngredientFactory: An instance of the ingredient factory.
    """
    return IngredientFactory(registered_ingredients=registered_ingredients)


@pytest.fixture
def ingredient_service(herb_repository, ingredient_factory):
    """Fixture for creating an IngredientService instance.

    Args:
        herb_repository (HerbJsonRepository): The herb repository fixture.
        ingredient_factory (IngredientFactory): The ingredient factory fixture.

    Returns:
        IngredientService: An instance of the ingredient service.
    """
    return IngredientService(
        ingredient_repository=herb_repository, ingredient_factory=ingredient_factory
    )
