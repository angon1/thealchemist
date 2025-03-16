from abc import ABC
from pydantic import BaseModel
from typing import Dict


class BaseIngredient(ABC, BaseModel):
    name: str
    desctiption: str = None
    # features : dict = {"feature": _strength_}
    features: Dict[str,int] = {"NoFeature": 0}

    def get_features(self):
        return self.features
