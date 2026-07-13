from typing import Protocol

from ex0.interface import Creature


class NormalCreature(Protocol):
    def attack(self):
        ...


class AggressiveCreature(NormalCreature):
    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


class DefensiveCreature(NormalCreature):
    def heal(self, target: Creature | None = None) -> str:
        ...
