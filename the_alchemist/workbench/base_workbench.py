from abc import ABC
from pydantic import BaseModel
from typing import List
from tools.base_tool import BaseTool
from ingredients.base_ingredient import BaseIngredient

class BaseWorkbench(ABC, BaseModel):
    tools: List[str]
    ingredients: List[str]

    def add_tool(self, tool):
        self.tools.append(tool.name)

    def remove_tool(self, tool):
        self.tools.remove(tool.name)

    def add_ingredients(self, ingredients:List[BaseIngredient]):
        for ingredient in ingredients:
            self.ingredients.append(ingredient.name)

    def remove_ingredients(self, ingredients:List[BaseIngredient]):
        for ingredient in ingredients:
            self.ingredients.remove(ingredient.name)

    def get_final_product(self):
        if len(self.ingredients) == 1:
            return self.ingredients[0]
        else:
            raise ValueError("Workbench contains more than one ingredient. Cannot determine final product.")


    def use_tool(self, tool:BaseTool, ingredients:List[BaseIngredient]):
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

