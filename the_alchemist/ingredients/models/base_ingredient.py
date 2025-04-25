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
        return self.features

    def to_dict(self):
        return {
            "category": self.category,
            "name": self.name,
            "description": self.description,
            "features": self.features,
        }

    def __str__(self):
        return f"{self.category}: {self.name}\n{self.description}\n Features: {self.features}"

    def __repr__(self):
        return f"{self.category} - {self.name} - {self.description} - {self.features}"
