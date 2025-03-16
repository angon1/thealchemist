from abc import ABC
from pydantic import BaseModel


class BaseIngredient(ABC, BaseModel):
    name: str
    desctiption: str = None
    # features : dict = {"feature": _strength_}
    features: dict = {"NoFeature": 0}

    def get_features(self):
        return self.features
