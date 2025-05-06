import pytest


def test_add_recipe_success(recipe_service, dummy_recipe_data):
    data = dummy_recipe_data["specific_ingredients_recipe"]
    recipe = recipe_service.add_recipe(data)
    assert recipe.product == "Relaxation Ointment"


def test_add_recipe_failure(recipe_service):
    data = {"recipe_type": "unknown"}
    with pytest.raises(Exception, match="Failed to add recipe"):
        recipe_service.add_recipe(data)


def test_get_all_recipes(recipe_service):
    recipes = recipe_service.get_all_recipes()
    assert isinstance(recipes, list)
    assert len(recipes) > 0


def test_get_recipe_by_name(recipe_service):
    recipe = recipe_service.get_recipe_by_name("Healing Potion")
    assert recipe is not None
    assert recipe.product == "Healing Potion"


def test_get_best_recipe_specific(recipe_service, dummy_recipe_data):
    ingredients = [
        {"name": "Lavender", "features": {}},
        {"name": "Rosemary", "features": {}},
    ]
    preparation_requirements = {"skill": "alchemy:3"}
    recipe = recipe_service.get_best_recipe(ingredients, preparation_requirements)
    assert recipe.product == "Relaxation Ointment"


def test_get_best_recipe_feature_based(recipe_service, dummy_recipe_data):
    ingredients = [
        {"name": "Mandrake", "features": {"healing": 3}},
        {"name": "Rosemary", "features": {"healing": 2}},
    ]
    preparation_requirements = {"skill": "alchemy:2"}
    recipe = recipe_service.get_best_recipe(ingredients, preparation_requirements)
    assert recipe.product == "Healing Potion"


def test_get_best_recipe_no_match(recipe_service):
    ingredients = [{"name": "Unknown", "features": {}}]
    preparation_requirements = {"skill": "alchemy:1"}
    recipe = recipe_service.get_best_recipe(ingredients, preparation_requirements)
    assert recipe is None
def test_get_best_recipe_specific_match(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mock_recipe.ingredients = ["Mandrake", "Lavender"]
    mock_recipe.check_if_can_prepare.return_value = {"success": True}
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[mock_recipe])

    ingredients = [{"name": "Mandrake"}, {"name": "Lavender"}]
    preparation_requirements = {"skill": "alchemy:3"}
    result = recipe_service.get_best_recipe(ingredients, preparation_requirements)

    assert result == mock_recipe


def test_get_best_recipe_feature_based(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mock_recipe.required_feature = "healing"
    mock_recipe.check_if_can_prepare.return_value = {"success": True}
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[mock_recipe])

    ingredients = [{"name": "Mandrake", "features": {"healing": 5}}]
    preparation_requirements = {"skill": "alchemy:2"}
    result = recipe_service.get_best_recipe(ingredients, preparation_requirements)

    assert result == mock_recipe


def test_get_best_recipe_no_match(recipe_service, mocker):
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[])

    ingredients = [{"name": "Mandrake"}]
    preparation_requirements = {"skill": "alchemy:2"}
    result = recipe_service.get_best_recipe(ingredients, preparation_requirements)

    assert result is None
def test_get_best_recipe_specific_match(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mock_recipe.ingredients = ["Mandrake", "Lavender"]
    mock_recipe.check_if_can_prepare.return_value = {"success": True}
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[mock_recipe])

    ingredients = [{"name": "Mandrake"}, {"name": "Lavender"}]
    skills = {"alchemy": 3}
    result = recipe_service.get_best_recipe(ingredients, skills)

    assert result == mock_recipe


def test_get_best_recipe_feature_based(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mock_recipe.required_feature = "healing"
    mock_recipe.check_if_can_prepare.return_value = {"success": True}
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[mock_recipe])

    ingredients = [{"name": "Mandrake", "features": {"healing": 5}}]
    skills = {"alchemy": 3}
    result = recipe_service.get_best_recipe(ingredients, skills)

    assert result == mock_recipe


def test_get_best_recipe_no_match(recipe_service, mocker):
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=[])

    ingredients = [{"name": "Mandrake"}]
    skills = {"alchemy": 3}
    result = recipe_service.get_best_recipe(ingredients, skills)

    assert result is None
import pytest
from recipes.service import RecipeService


def test_get_recipe_by_name(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mocker.patch.object(recipe_service.recipe_repository, "get_by_name", return_value=mock_recipe)

    result = recipe_service.get_recipe_by_name("Healing Potion")
    assert result == mock_recipe
    recipe_service.recipe_repository.get_by_name.assert_called_once_with("Healing Potion")


def test_add_recipe_success(recipe_service, mocker):
    mock_recipe = mocker.Mock()
    mocker.patch.object(recipe_service.recipe_factory, "create", return_value=mock_recipe)
    mocker.patch.object(recipe_service.recipe_repository, "add")

    data = {"recipe_type": "feature_based", "product": "Healing Potion"}
    result = recipe_service.add_recipe(data)

    assert result == mock_recipe
    recipe_service.recipe_factory.create.assert_called_once_with(data)
    recipe_service.recipe_repository.add.assert_called_once_with(mock_recipe)


def test_add_recipe_failure(recipe_service, mocker):
    mocker.patch.object(recipe_service.recipe_factory, "create", side_effect=Exception("Creation error"))

    data = {"recipe_type": "feature_based", "product": "Healing Potion"}
    with pytest.raises(Exception, match="Failed to add recipe: Creation error"):
        recipe_service.add_recipe(data)


def test_get_all_recipes(recipe_service, mocker):
    mock_recipes = [mocker.Mock(), mocker.Mock()]
    mocker.patch.object(recipe_service.recipe_repository, "get_all", return_value=mock_recipes)

    result = recipe_service.get_all_recipes()
    assert result == mock_recipes
    recipe_service.recipe_repository.get_all.assert_called_once()
