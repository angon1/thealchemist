from abc import ABC
from pydantic import BaseModel
from typing import List
from tools.base_tool import BaseTool
from ingredients.models.base_ingredient import BaseIngredient

class BaseProcedure(ABC, BaseModel):
    required_tools: List[str]
    required_ingredients: List[str]


