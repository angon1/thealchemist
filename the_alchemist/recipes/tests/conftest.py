import pytest
from recipes.factory.recipe_factory import RecipeFactory
from recipes.repositories.recipe_json_repository import RecipeJsonRepository
from recipes.service import RecipeService
from the_alchemist.settings import settings


@pytest.fixture
def recipe_repository():
    return RecipeJsonRepository(file_path=settings.DEFAULT_JSON_DB_PATH)


@pytest.fixture
def recipe_factory():
    return RecipeFactory()


@pytest.fixture
def recipe_service(recipe_repository, recipe_factory):
    return RecipeService(
        recipe_repository=recipe_repository, recipe_factory=recipe_factory
    )