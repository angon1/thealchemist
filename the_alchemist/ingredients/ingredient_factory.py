from ingredients.herb import Herb

INGREDIENT_CATEGORIES = {"herb": Herb}


class IngredientFactory:
    @staticmethod
    def produce_ingredient(data: dict):
        ingredient_class = INGREDIENT_CATEGORIES.get(data.pop("category"))
        if ingredient_class:
            return ingredient_class(**data)
        else:
            raise ValueError("Invalid ingredient type")
