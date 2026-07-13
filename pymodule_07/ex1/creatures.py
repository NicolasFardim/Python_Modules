from ex0.interface import Creature
from .interface import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self, target: Creature | None = None) -> str:
        if target:
            return f"{self._name} heals {target._name} for a small amount"
        else:
            return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self, target: Creature | None = None) -> str:
        if target:
            return f"{self._name} heals {target._name} and others for a large amount"
        else:
            return f"{self._name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._transformed:
            return f"{self._name} attacks normally!"
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self._transformed:
            return f"{self._name} attacks normally!"
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form"
