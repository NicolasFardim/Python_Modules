from typing import Any, cast

from ex0.interface import Creature
from ex1.interface import HealCapability, TransformCapability
from .interface import BattleStrategy
from .protocols import AggressiveCreature, DefensiveCreature


class InvalidStrategy(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Normal")

    def act(self, creature: Any) -> str:
        if self.is_valid(creature):
            return creature.attack()
        else:
            raise InvalidStrategy("Invalid 'non Creature' for this normal strategy.")

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Aggressive")

    def act(self, creature: Any) -> str:
        if self.is_valid(creature):
            aggressive_creature = cast(AggressiveCreature, creature)
            return "\n".join((
                aggressive_creature.transform(),
                aggressive_creature.attack(),
                aggressive_creature.revert()
            ))
        else:
            raise InvalidStrategy(f"Invalid '{creature.get_name()}' for this aggressive strategy.")

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        super().__init__("Defensive")

    def act(self, creature: Any):
        if self.is_valid(creature):
            heal_creature = cast(DefensiveCreature, creature)
            return "\n".join((
                heal_creature.attack(),
                heal_creature.heal()
            ))
        else:
            raise InvalidStrategy(f"Invalid '{creature.get_name()}' for this defensive strategy.")

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, HealCapability)
