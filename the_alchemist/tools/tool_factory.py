from tools.simple_tool import SimpleTool


class IngredientFactory:
    @staticmethod
    def create(data: dict):
        try:
            return SimpleTool(**data)
        except Exception as e:
            raise Exception(f"Failed to create tool: {e}")
