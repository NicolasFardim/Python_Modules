from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self._name: str = name
        self._creature_type: str = creature_type

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._creature_type} type Creature"


class CreatureFactory(ABC):
    def __init__(self, factory_name) -> None:
        self._factory_name = factory_name

    def get_name(self) -> str:
        return self._factory_name

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...
