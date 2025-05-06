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
