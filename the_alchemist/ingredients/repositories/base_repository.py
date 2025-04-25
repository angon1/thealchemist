from abc import ABC, abstractmethod

from ingredients.models.base_ingredient import BaseIngredient


class BaseIngredientRepository(ABC):
    model: BaseIngredient

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, name: str) -> BaseIngredient:
        raise NotImplementedError

    @abstractmethod
    def add(self, instance: BaseIngredient) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[BaseIngredient]:
        """
        Get all ingredients.
        """
        raise NotImplementedError
