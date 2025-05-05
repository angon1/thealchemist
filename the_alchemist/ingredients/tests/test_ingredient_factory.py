def test_create_ingredient_success(ingredient_factory):
    data = {
        "category": "herb",
        "name": "Sage",
        "description": "A herb with medicinal properties.",
        "features": {"healing": 5},
    }
    ingredient = ingredient_factory.create(data)
    assert ingredient.name == "Sage"
    assert ingredient.features["healing"] == 5


def test_create_ingredient_failure(ingredient_factory):
    data = {
        "category": "unknown",
        "name": "Unknown",
        "description": "An unknown ingredient.",
    }
    try:
        ingredient_factory.create(data)
    except Exception as e:
        assert "Failed to create ingredient" in str(e)
