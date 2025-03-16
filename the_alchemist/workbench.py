from abc import ABC, abstractmethod
from pydantic import BaseModel
from ingredients.base_ingredient import BaseIngredient
from typing import List, Optional
from collections import Counter

class BaseTool(ABC, BaseModel):
    name: str
    description: Optional[str] = None
    allowed_ingredients: list = []

    @abstractmethod
    def use(self, ingredients: List[BaseIngredient]):
        raise NotImplementedError("The method 'use' must be implemented.")

class BaseProcedure(ABC, BaseModel):
    name: str
    description: str = None
    steps: list = []
    required_tools: set = set()
    required_ingredients: Counter = Counter()

    @abstractmethod
    def verify(self, workbench: 'Workbench'):
        raise NotImplementedError("The method 'verify' must be implemented.")

    @abstractmethod
    def execute(self, workbench: 'Workbench'):
        raise NotImplementedError("The method 'verify' must be implemented.")

class Workbench:
    def __init__(self):
        self.__tools : set[BaseTool] = set()
        self.__ingredients : List[BaseIngredient] = []
        self.__procedure : BaseProcedure = None

    def add_tool(self, tool):
        self.__tools.append(tool)

    def remove_tool(self, tool):
        self.__tools.remove(tool)

    def use_tools(self):
        for tool in self.__tools:
            if hasattr(tool, 'use') and callable(getattr(tool, 'use')):
                tool.use()
            else:
                raise Exception(f"The tool {tool} does not have a 'use' method.")

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.__ingredients.remove(ingredient)

    def add_procedure(self, procedure):
        self.__procedure = procedure

    def remove_procedure(self):
        self.__procedure = None

    def verify_procedure(self):
        if self.__procedure is None:
            raise Exception("No procedure to verify.")
        return self.__procedure.verify(self)
    
    def execute_procedure(self):
        if self.__procedure is None:
            raise Exception("No procedure to execute.")
        try:
            return self.__procedure.execute(self)
        except Exception as e:
            raise Exception(f"An error occurred while executing the procedure: {e}") from e


