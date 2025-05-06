from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from pydantic import BaseModel


class BaseRecipe(ABC, BaseModel):
    """BaseRecipe is an abstract base class for recipes.

    Attributes:
        ingredients (List[str]): A list of ingredient names required for the recipe.
        category (str): The category of the recipe.
        product (str): The name of the resulting product.
        minimum_skills_level (Optional[Dict[str, int]]): Minimum skill levels required for the recipe.
        modifiers (Optional[Dict[str, int]]): Modifiers for the recipe.
    """
    ingredients: List[str]
    category: str
    product: str
    minimum_skills_level: Optional[Dict[str, int]] = None
    modifiers: Optional[Dict[str, int]] = None

    @abstractmethod
    def process(self, ingredients: List[dict]) -> dict:
        """Process the recipe with the given ingredients.

        Args:
            ingredients (List[dict]): A list of ingredient data.

        Returns:
            dict: The resulting product data.
        """
        raise NotImplementedError("The method 'process' must be implemented.")

    @abstractmethod
    def check_if_can_prepare(self, ingredients: List[dict], skills: Dict[str, int]) -> Dict:
        """Check if the recipe can be prepared with the given ingredients and skills.

        Args:
            ingredients (List[dict]): A list of ingredient data.
            skills (Dict[str, int]): A dictionary of skill levels.

        Returns:
            Dict: A dictionary indicating success or failure and the reason if failed.
        """
        raise NotImplementedError("The method 'check_if_can_prepare' must be implemented.")

    @abstractmethod
    def apply_modifiers(self, product_data: dict, skills: Dict[str, int]) -> dict:
        """Apply modifiers to the product based on skills.

        Args:
            product_data (dict): The initial product data.
            skills (Dict[str, int]): A dictionary of skill levels.

        Returns:
            dict: The modified product data.
        """
        raise NotImplementedError("The method 'apply_modifiers' must be implemented.")

    @abstractmethod
    def get_product(self, ingredients: List[dict], skills: Dict[str, int]) -> Dict:
        """Generate the final product based on the recipe.

        Args:
            ingredients (List[dict]): A list of ingredient data.
            skills (Dict[str, int]): A dictionary of skill levels.

        Returns:
            Dict: A dictionary containing the product data or failure reason.
        """
        raise NotImplementedError("The method 'get_product' must be implemented.")

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
            f"Ingredients: {self.ingredients} - "
            f"Minimum Skills Level: {self.minimum_skills_level} - "
            f"Modifiers: {self.modifiers}"
        )