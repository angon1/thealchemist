from ingredients.ingredient import Ingredient


class IngredientFactory:
    @staticmethod
    def create(data: dict):
        try:
            return Ingredient(**data)
        except Exception as e:
            raise Exception(f"Failed to create ingredient: {e}")
