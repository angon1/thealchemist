class IngredientService:
    def __init__(
        self,
        registered_ingredients=None,
        category=None,
        ingredient_repository=None,
        ingredient_factory=None,
    ):
        self.ingredient_repository = ingredient_repository
        self.ingredient_factory = ingredient_factory

    def get_ingredient_by_name(self, name: str):
        """
        Get an ingredient by its name.
        """
        return self.ingredient_repository.get_by_name(name)

    def add_ingredient(self, data: dict):
        """
        Add a new ingredient.
        """
        try:
            ingredient = self.ingredient_factory.create(data)
            self.ingredient_repository.add(ingredient)
            return ingredient
        except Exception as e:
            raise Exception(f"Failed to add ingredient: {e}")

    def get_all_ingredients(self):
        """
        Get all ingredients.
        """
        return self.ingredient_repository.get_all()

    def get_ingriedients_names(self):
        """
        Get all ingredients names.
        """
        return [ingredient.name for ingredient in self.ingredient_repository.get_all()]
