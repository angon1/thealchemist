def test_add_ingredient(ingredient_service):
    data = {
        "category": "herb",
        "name": "Thyme",
        "description": "A fragrant herb used in cooking.",
        "features": {"flavor": 4},
    }
    ingredient = ingredient_service.add_ingredient(data)
    assert ingredient.name == "Thyme"
    assert ingredient_service.get_ingredient_by_name("Thyme").name == "Thyme"


def test_get_all_ingredients(ingredient_service):
    ingredients = ingredient_service.get_all_ingredients()
    assert isinstance(ingredients, list)
    assert len(ingredients) > 0


def test_get_ingredient_by_name(ingredient_service):
    ingredient = ingredient_service.get_ingredient_by_name("Mandrake")
    assert ingredient is not None
    assert ingredient.name == "Mandrake"


def test_get_ingredients_names(ingredient_service):
    names = ingredient_service.get_ingriedients_names()
    assert isinstance(names, list)
    assert "Mandrake" in names
