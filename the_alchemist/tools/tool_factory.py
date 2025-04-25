from tools.simple_tool import SimpleTool


class IngredientFactory:
    """
    A factory class for creating tool instances.

    Methods:
        create(data: dict):
            Creates an instance of SimpleTool using the provided data dictionary.
            Args:
                data (dict): A dictionary containing the data required to create a SimpleTool instance.
            Returns:
                SimpleTool: An instance of SimpleTool created with the provided data.
            Raises:
                Exception: If the tool creation fails, an exception is raised with an error message.
    """
    @staticmethod
    def create(data: dict):
        try:
            return SimpleTool(**data)
        except Exception as e:
            raise Exception(f"Failed to create tool: {e}")
