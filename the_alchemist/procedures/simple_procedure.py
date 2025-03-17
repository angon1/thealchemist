from procedures.base_procedure import BaseProcedure

class SimpleProcedure(BaseProcedure):
    def verify(self, workbench):
        print(workbench)
        print(f"Verifying the simple procedure {self.name}.")
        return True

    def execute(self, workbench):
        print(workbench)
        print(f"Executing the simple procedure {self.name}.")
        return True