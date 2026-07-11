from .creatures import Flameling, Pyrodon, Torragon, Aquabub
from .interface import CreatureFactory, Creature


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self):
        return Torragon()
