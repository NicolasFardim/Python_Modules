from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def act(self, creature: Any) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...
