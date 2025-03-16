from pydantic import BaseModel
from abc import ABC


class BaseProduct(ABC, BaseModel):
    name: str
    description: str = None
    features: dict = {"NoFeature": 0}
    allowed_actions: list = []

    def get_features(self):
        return self.features

    def get_actions(self):
        return self.allowed_actions