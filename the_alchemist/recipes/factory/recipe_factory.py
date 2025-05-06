class RecipeFactory:
    def __init__(self, registered_recipes=None, recipe_type_field=None):
        self.registered_recipes = registered_recipes or None
        self.recipe_type_field = recipe_type_field or "recipe_type"

    def create(self, data: dict):
        try:
            recipe_type = data.get(self.recipe_type_field, None)
            return self.registered_recipes.get(recipe_type)(**data)
        except Exception as e:
            raise Exception(f"Failed to create recipe: {e}")
