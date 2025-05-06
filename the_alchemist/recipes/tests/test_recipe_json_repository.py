def test_get_by_name(recipe_repository):
    recipe = recipe_repository.get_by_name("Healing Potion")
    assert recipe is not None
    assert recipe.product == "Healing Potion"


def test_get_all(recipe_repository):
    recipes = recipe_repository.get_all()
    assert isinstance(recipes, list)
    assert len(recipes) > 0


def test_add_recipe(recipe_repository, dummy_recipe_data):
    data = dummy_recipe_data["specific_ingredients_recipe"]
    from recipes.models.specific_ingredients_recipe import SpecificIngredientsRecipe

    recipe = SpecificIngredientsRecipe(**data)
    recipe_repository.add(recipe)
    added_recipe = recipe_repository.get_by_name("Relaxation Ointment")
    assert added_recipe is not None
    assert added_recipe.product == "Relaxation Ointment"