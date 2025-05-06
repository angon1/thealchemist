import pytest


def test_create_specific_ingredients_recipe(recipe_factory, dummy_recipe_data):
    data = dummy_recipe_data["specific_ingredients_recipe"]
    recipe = recipe_factory.create(data)
    assert recipe.product == "Relaxation Ointment"
    assert recipe.ingredients == ["Lavender", "Rosemary"]


def test_create_feature_based_recipe(recipe_factory, dummy_recipe_data):
    data = dummy_recipe_data["feature_based_recipe"]
    recipe = recipe_factory.create(data)
    assert recipe.product == "Healing Potion"
    assert recipe.required_feature == "healing"


def test_create_recipe_failure(recipe_factory):
    data = {"recipe_type": "unknown"}
    with pytest.raises(Exception, match="Failed to create recipe"):
        recipe_factory.create(data)