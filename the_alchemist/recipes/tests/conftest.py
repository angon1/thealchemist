import pytest
from recipes.factory.recipe_factory import RecipeFactory
from recipes.repositories.recipe_json_repository import RecipeJsonRepository
from recipes.service import RecipeService
from the_alchemist.settings import settings


@pytest.fixture
def recipe_repository():
    """Fixture for creating a RecipeJsonRepository instance."""
    return RecipeJsonRepository(file_path=settings.DEFAULT_JSON_RECIPE_DB_PATH)


@pytest.fixture
def recipe_factory():
    """Fixture for creating a RecipeFactory instance."""
    from recipes.db.mappings import registered_recipe_types
    return RecipeFactory(registered_recipes=registered_recipe_types)


@pytest.fixture
def recipe_service(recipe_repository, recipe_factory):
    """Fixture for creating a RecipeService instance."""
    return RecipeService(
        recipe_repository=recipe_repository, recipe_factory=recipe_factory
    )


@pytest.fixture
def dummy_recipe_data():
    """Fixture for providing dummy recipe data."""
    return {
        "specific_ingredients_recipe": {
            "recipe_type": "specific_ingredients",
            "ingredients": ["Lavender", "Rosemary"],
            "category": "ointment",
            "product": "Relaxation Ointment",
            "preparation_requirements": {"skill": "alchemy:3"},
            "modifiers": {"aroma": 2},
            "product_data": {
                "category": "ointment",
                "name": "Relaxation Ointment",
                "features": {"aroma": 10, "healing": 2},
            },
        },
        "feature_based_recipe": {
            "recipe_type": "feature_based",
            "required_feature": "healing",
            "category": "potion",
            "product": "Healing Potion",
            "preparation_requirements": {"skill": "alchemy:2"},
            "modifiers": {"healing": 5},
        },
    }