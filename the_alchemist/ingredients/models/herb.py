from ingredients.models.base_ingredient import BaseIngredient


class Herb(BaseIngredient):
    category: str = "herb"
