from abc import ABC
from pydantic import BaseModel
from typing import List
from tools.base_tool import BaseTool
from ingredients.models.base_ingredient import BaseIngredient

class BaseWorkbench(ABC, BaseModel):
    """
    BaseWorkbench is an abstract base class that represents a workbench used for combining tools and ingredients to create a final product.

    Attributes:
        tools (List[str]): A list of tool names available in the workbench.
        ingredients (List[str]): A list of ingredient names available in the workbench.

    Methods:
        add_tool(tool):
            Adds a tool to the workbench.
        
        remove_tool(tool):
            Removes a tool from the workbench.
        
        add_ingredients(ingredients: List[BaseIngredient]):
            Adds a list of ingredients to the workbench.
        
        remove_ingredients(ingredients: List[BaseIngredient]):
            Removes a list of ingredients from the workbench.
        
        get_final_product():
            Returns the final product if there is exactly one ingredient in the workbench.
            Raises a ValueError if there is more than one ingredient.
        
        use_tool(tool: BaseTool, ingredients: List[BaseIngredient]):
            Uses a tool on a list of ingredients to produce a final product.
            Raises a ValueError if any ingredient is not found in the workbench or if the tool is not found in the workbench.
    """
    tools: List[str]
    ingredients: List[str]
    recipes: List[dict] = []
    product: str = None

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
