from abc import ABC, abstractmethod
from pydantic import BaseModel
from ingredients.models.base_ingredient import BaseIngredient
from typing import List


class BaseTool(ABC, BaseModel):
    name: str
    allowed_ingredient_types: List[str] = []

    @abstractmethod
    def use(self, ingredients: List[BaseIngredient]):
        raise NotImplementedError("The method 'use' must be implemented.")
