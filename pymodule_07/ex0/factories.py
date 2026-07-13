from .creatures import Flameling, Pyrodon, Torragon, Aquabub
from .interface import CreatureFactory


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Flameling")

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__("Aquabub")

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
