from typing import Protocol

from ex0.interface import Creature


class NormalCreature(Protocol):
    def attack(self) -> str:
        ...


class AggressiveCreature(NormalCreature, Protocol):
    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class DefensiveCreature(NormalCreature, Protocol):
    def heal(self, target: Creature | None = None) -> str:
        ...
