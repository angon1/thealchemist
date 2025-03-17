from abc import ABC, abstractmethod
from pydantic import BaseModel
from workbench.base_workbench import BaseWorkbench
from tools.base_tool import BaseTool
from ingredients.base_ingredient import BaseIngredient
from typing import List, Set



class BaseProcedure(ABC, BaseModel):
    name: str
    description: str = None
    steps: list = []
    required_tools: Set[BaseTool] = set()
    required_ingredients: List[BaseIngredient] = []

    @abstractmethod
    def verify(self, workbench: "BaseWorkbench"):
        raise NotImplementedError("The method 'verify' must be implemented.")

    @abstractmethod
    def execute(self, workbench: "BaseWorkbench"):
        raise NotImplementedError("The method 'verify' must be implemented.")
    

