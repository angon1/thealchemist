from typing import List, Optional, Dict
from recipes.models.specific_ingredients_recipe import SpecificIngredientsRecipe
from recipes.models.feature_based_recipe import FeatureBasedRecipe


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

    def get_best_recipe(self, ingredients: List[dict], preparation_requirements: Dict[str, str]) -> Optional[dict]:
        """
        Find the best fitting recipe based on the given ingredients and preparation requirements.

        Args:
            ingredients (List[dict]): A list of ingredient data.
            preparation_requirements (Dict[str, str]): A dictionary of preparation requirements.

        Returns:
            Optional[dict]: The best fitting recipe or None if no recipe matches.
        """
        # Step 1: Find all SpecificIngredientsRecipes that match the ingredients
        specific_recipes = [
            recipe for recipe in self.recipe_repository.get_all()
            if isinstance(recipe, SpecificIngredientsRecipe) and set(recipe.ingredients) == {i["name"] for i in ingredients}
        ]

        # Step 2: Check if any specific recipe can be prepared
        for recipe in specific_recipes:
            if recipe.check_if_can_prepare(ingredients, preparation_requirements)["success"]:
                return recipe

        # Step 3: Find FeatureBasedRecipes and evaluate by strongest feature totals
        feature_recipes = [
            recipe for recipe in self.recipe_repository.get_all()
            if isinstance(recipe, FeatureBasedRecipe)
        ]

        # Sort features by their total strength in descending order
        for feature in sorted(
            {f for r in feature_recipes for f in r.required_feature},
            key=lambda f: sum(i["features"].get(f, 0) for i in ingredients),
            reverse=True,
        ):
            for recipe in feature_recipes:
                if recipe.required_feature == feature:
                    if recipe.check_if_can_prepare(ingredients, preparation_requirements)["success"]:
                        return recipe

        # No matching recipe found
        return None