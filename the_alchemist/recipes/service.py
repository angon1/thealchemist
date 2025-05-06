class RecipeService:
    def __init__(self, recipe_repository=None, recipe_factory=None):
        self.recipe_repository = recipe_repository
        self.recipe_factory = recipe_factory

    def get_recipe_by_name(self, name: str):
        """Retrieve a recipe by its name."""
        return self.recipe_repository.get_by_name(name)

    def add_recipe(self, data: dict):
        """Add a new recipe."""
        try:
            recipe = self.recipe_factory.create(data)
            self.recipe_repository.add(recipe)
            return recipe
        except Exception as e:
            raise Exception(f"Failed to add recipe: {e}")

    def get_all_recipes(self):
        """Retrieve all recipes."""
        return self.recipe_repository.get_all()