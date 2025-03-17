import pytest
from pydantic import BaseModel
from typing import List
from tools.simple_tool import BaseTool

class MockTool(BaseTool):
    def use(self, ingredients: List[str]):
        return "product"

class MockIngredient(BaseModel):
    name: str


def test_add_tool(workbench):
    tool = MockTool(name="hammer")
    workbench.add_tool(tool)
    assert "hammer" in workbench.tools

def test_remove_tool(workbench):
    tool = MockTool(name="hammer")
    workbench.add_tool(tool)
    workbench.remove_tool(tool)
    assert "hammer" not in workbench.tools

def test_use_tool_success(workbench):
    tool = MockTool(name="hammer")
    ingredient = MockIngredient(name="wood")
    workbench.add_tool(tool)
    workbench.ingredients.append("wood")
    product = workbench.use_tool(tool, [ingredient])
    assert product == "product"
    assert "wood" not in workbench.ingredients
    assert "product" in workbench.ingredients

def test_use_tool_missing_ingredient(workbench):
    tool = MockTool(name="hammer")
    ingredient = MockIngredient(name="wood")
    workbench.add_tool(tool)
    with pytest.raises(ValueError, match="Ingredient name='wood' not found in workbench."):
        workbench.use_tool(tool, [ingredient])

def test_use_tool_missing_tool(workbench):
    tool = MockTool(name="hammer")
    ingredient = MockIngredient(name="wood")
    workbench.ingredients.append("wood")
    with pytest.raises(ValueError, match="Tool hammer not found in workbench."):
        workbench.use_tool(tool, [ingredient])

def test_workbench_initialization():
    from workbench.workbench import Workbench
    workbench = Workbench(tools=[], ingredients=[])
    assert workbench.tools == []
    assert workbench.ingredients == []

def test_add_ingredients(workbench):
    ingredient = MockIngredient(name="wood")
    workbench.add_ingredients([ingredient])
    assert "wood" in workbench.ingredients

def test_remove_ingredients(workbench):
    ingredient = MockIngredient(name="wood")
    workbench.add_ingredients([ingredient])
    workbench.remove_ingredients([ingredient])
    assert "wood" not in workbench.ingredients

def test_get_final_product_single_ingredient(workbench):
    ingredient = MockIngredient(name="wood")
    workbench.add_ingredients([ingredient])
    product = workbench.get_final_product()
    assert product == "wood"

def test_get_final_product_multiple_ingredients(workbench):
    ingredient1 = MockIngredient(name="wood")
    ingredient2 = MockIngredient(name="stone")
    workbench.add_ingredients([ingredient1, ingredient2])
    with pytest.raises(ValueError, match="Workbench contains more than one ingredient. Cannot determine final product."):
        workbench.get_final_product()