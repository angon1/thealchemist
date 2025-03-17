from workbench.workbench import Workbench

class WorkbenchFactory:
    @staticmethod
    def create(data: dict):
        try:
            return Workbench(**data)
        except Exception as e:
            raise Exception(f"Failed to create tool: {e}")
