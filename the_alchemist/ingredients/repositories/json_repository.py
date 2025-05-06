from __future__ import annotations

import json
from pathlib import Path

from .base_repository import BaseIngredientRepository


class JsonRepository(BaseIngredientRepository):
    def __init__(self, file_path: str):
        if file_path is None:
            raise ValueError("File path cannot be None")
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        self.file_path = Path(file_path).resolve()
        self.data = self.load_data()

    def load_data(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
            return data

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def add(self, instance: BaseIngredient):
        print(f"\n\n\instance type ={type(instance)}\n {instance.name}\n\n\n")
        self.data[instance.name] = instance.to_dict()
        self.save_data(self.data)
