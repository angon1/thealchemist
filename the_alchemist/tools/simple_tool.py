from tools.base_tool import BaseTool


class SimpleTool(BaseTool):
    def use(self):
        print(f"Using the simple tool {self.name}.")
