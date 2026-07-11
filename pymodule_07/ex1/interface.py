from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        ...
