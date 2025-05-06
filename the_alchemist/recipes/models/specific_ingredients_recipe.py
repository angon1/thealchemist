from .base_recipe import BaseRecipe
from typing import List, Dict


class SpecificIngredientsRecipe(BaseRecipe):
    """A recipe that processes specific ingredients to produce a unique product.

    Attributes:
        product_data (dict): The data for the resulting product.
    """
    product_data: Dict

    def process(self, ingredients: List[dict]) -> dict:
        """Process the recipe by verifying specific ingredients and returning a unique product.

        Args:
            ingredients (List[dict]): A list of ingredient data.

        Returns:
            dict: The resulting product data.

        Raises:
            ValueError: If the required ingredients are not provided.
        """
        ingredient_names = {ingredient["name"] for ingredient in ingredients}
        if set(self.ingredients) != ingredient_names:
            raise ValueError("The provided ingredients do not match the required ones.")
        return self.product_data

    def check_if_can_prepare(self, ingredients: List[dict], skills: Dict[str, int]) -> Dict:
        """Check if the recipe can be prepared with the given ingredients and skills."""
        ingredient_names = {ingredient["name"] for ingredient in ingredients}
        if set(self.ingredients) != ingredient_names:
            return {"success": False, "reason": "Ingredients do not match the required ones."}

        if self.minimum_skills_level:
            for skill, level in self.minimum_skills_level.items():
                if skills.get(skill, 0) < level:
                    return {"success": False, "reason": f"Skill '{skill}' too low."}
        return {"success": True}

    def apply_modifiers(self, product_data: dict, skills: Dict[str, int]) -> dict:
        """Apply modifiers to the product based on skills."""
        if self.modifiers:
            for modifier, value in self.modifiers.items():
                product_data["features"][modifier] = product_data["features"].get(modifier, 0) + value
        return product_data

    def get_product(self, ingredients: List[dict], skills: Dict[str, int]) -> Dict:
        """Generate the final product based on the recipe."""
        check = self.check_if_can_prepare(ingredients, skills)
        if not check["success"]:
            return check

        product_data = self.product_data.copy()
        product_data = self.apply_modifiers(product_data, skills)
        return {"success": True, "product": product_data}

    def to_dict(self):
        """Convert the recipe to a dictionary representation.

        Returns:
            dict: A dictionary containing the recipe's attributes.
        """
        return {
            "ingredients": self.ingredients,
            "category": self.category,
            "product": self.product,
            "minimum_skills_level": self.minimum_skills_level,
            "modifiers": self.modifiers,
            "product_data": self.product_data,
        }

    def __str__(self):
        """Generate a string representation of the recipe.

        Returns:
            str: A string describing the recipe.
        """
        return (
            f"Category: {self.category}\n"
            f"Product: {self.product}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Minimum Skills Level: {self.minimum_skills_level}\n"
            f"Modifiers: {self.modifiers}\n"
            f"Product Data: {self.product_data}"
        )

    def __repr__(self):
        """Generate a detailed string representation of the recipe.

        Returns:
            str: A detailed string describing the recipe.
        """
        return (
            f"Category: {self.category} - "
            f"Product: {self.product} - "
            f"Ingredients: {self.ingredients} - "
            f"Minimum Skills Level: {self.minimum_skills_level} - "
            f"Modifiers: {self.modifiers} - "
            f"Product Data: {self.product_data}"
        )
