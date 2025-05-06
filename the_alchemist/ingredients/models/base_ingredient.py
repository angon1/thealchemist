from abc import ABC
from typing import Dict

from pydantic import BaseModel


class BaseIngredient(ABC, BaseModel):
    category: str
    name: str
    description: str = None
    # features : dict = {"feature": _strength_}
    features: Dict[str, int] = {"NoFeature": 0}

    def get_features(self):
        """Retrieve the features of the ingredient.

        Returns:
            Dict[str, int]: A dictionary of features and their values.
        """
        return self.features

    def to_dict(self):
        """Convert the ingredient to a dictionary representation.

        Returns:
            dict: A dictionary containing the ingredient's attributes.
        """
        return {
            "category": self.category,
            "name": self.name,
            "description": self.description,
            "features": self.features,
        }

    def __str__(self):
        """Generate a string representation of the ingredient.

        Returns:
            str: A string describing the ingredient.
        """
        return f"{self.category}: {self.name}\n{self.description}\n Features: {self.features}"

    def __repr__(self):
        """Generate a detailed string representation of the ingredient.

        Returns:
            str: A detailed string describing the ingredient.
        """
        return f"{self.category} - {self.name} - {self.description} - {self.features}"
