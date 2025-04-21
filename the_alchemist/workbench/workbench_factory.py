from workbench.workbench import Workbench

class WorkbenchFactory:
    """
    Factory class for creating Workbench instances.
    """

    @staticmethod
    def create(data: dict):
        """
        Create a Workbench instance from a dictionary of data.

        Args:
            data (dict): A dictionary containing the data to initialize the Workbench.

        Returns:
            Workbench: An instance of the Workbench class initialized with the provided data.

        Raises:
            Exception: If the Workbench instance cannot be created.
        """

        try:
            return Workbench(**data)
        except Exception as e:
            raise Exception(f"Failed to create workbench: {e}")
