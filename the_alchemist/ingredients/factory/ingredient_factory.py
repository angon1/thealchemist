class IngredientFactory:
    def __init__(self, registered_ingredients=None, category=None):
        self.registered_ingredients = registered_ingredients or None
        self.category_field = category or "category"

    def create(self, data: dict):
        try:
            category = data.get(self.category_field, None)
            print(data)
            return self.registered_ingredients.get(category)(**data)
        except Exception as e:
            raise Exception(f"Failed to create ingredient: {e}")
