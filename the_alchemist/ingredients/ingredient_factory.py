from ingredients.mappings import INGREDIENT_CATEGORIES

class IngredientFactory:
    @staticmethod
    def produce_ingredient(data: dict):
        ingredient_class = INGREDIENT_CATEGORIES.get(data.pop("category"))
        if ingredient_class:
            return ingredient_class(**data)
        else:
            raise ValueError("Invalid ingredient type")
