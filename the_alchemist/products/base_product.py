from pydantic import BaseModel
from abc import ABC


class BaseProduct(ABC, BaseModel):
    name: str
    category: str = None
    description: str = None
    features: dict = {"NoFeature": 0}


    def get_features(self):
        return self.features
