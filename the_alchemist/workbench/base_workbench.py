from abc import ABC
from pydantic import BaseModel
from typing import List
from tools.base_tool import BaseTool

class BaseWorkbench(ABC, BaseModel):
    tools: List[str]
    ingredients: List[str]

    def add_tool(self, tool):
        self.tools.append(tool.name)

    def remove_tool(self, tool):
        self.tools.remove(tool.name)

    def use_tool(self, tool:BaseTool, ingredients:List[str]):
        for ingredient in ingredients:
            if ingredient.name not in self.ingredients:
                raise ValueError(f"Ingredient {ingredient} not found in workbench.")
            self.ingredients.remove(ingredient.name)
        if tool.name in self.tools:
            product = tool.use(ingredients)
            self.ingredients.append(product)
            return product
        else:
            raise ValueError(f"Tool {tool.name} not found in workbench.")

