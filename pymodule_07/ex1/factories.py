from ex0.interface import CreatureFactory
from .creatures import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        pass

    def create_evolved(self):
        pass
