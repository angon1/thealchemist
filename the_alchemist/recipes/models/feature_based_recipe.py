from .base_recipe import BaseRecipe
from typing import List, Dict


class FeatureBasedRecipe(BaseRecipe):
    """A recipe that processes ingredients based on their features.

    Attributes:
        required_feature (str): The feature required for the recipe.
    """
    required_feature: str
    ingredients: List[str] = []  # Override to make it optional

    def check_if_can_prepare(self, ingredients: List[dict], skills: Dict[str, int]) -> Dict:
        """Check if the recipe can be prepared with the given ingredients and skills."""
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

        total_strength = sum(
            ingredient["features"].get(self.required_feature, 0)
            for ingredient in ingredients
        )
        product_data = {
            "category": self.category,
            "name": self.product,
            "features": {self.required_feature: total_strength},
        }
        product_data = self.apply_modifiers(product_data, skills)
        return {"success": True, "product": product_data}

    def to_dict(self):
        """Convert the recipe to a dictionary representation.

        Returns:
            dict: A dictionary containing the recipe's attributes.
        """
        return {
            "required_feature": self.required_feature,
            "category": self.category,
            "product": self.product,
            "minimum_skills_level": self.minimum_skills_level,
            "modifiers": self.modifiers,
        }

    def __str__(self):
        """Generate a string representation of the recipe.

        Returns:
            str: A string describing the recipe.
        """
        return (
            f"Category: {self.category}\n"
            f"Product: {self.product}\n"
            f"Required Feature: {self.required_feature}\n"
            f"Minimum Skills Level: {self.minimum_skills_level}\n"
            f"Modifiers: {self.modifiers}"
        )

    def __repr__(self):
        """Generate a detailed string representation of the recipe.

        Returns:
            str: A detailed string describing the recipe.
        """
        return (
            f"Category: {self.category} - "
            f"Product: {self.product} - "
            f"Required Feature: {self.required_feature} - "
            f"Minimum Skills Level: {self.minimum_skills_level} - "
            f"Modifiers: {self.modifiers}"
        )
