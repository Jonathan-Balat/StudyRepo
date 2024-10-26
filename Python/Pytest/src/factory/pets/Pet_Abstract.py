from abc import ABC, abstractmethod

# This limits what content can be imported from this file.
__all__ = ['PetAbstract']


class PetAbstract(ABC):

    @abstractmethod
    def has_name(self):
        pass

    @abstractmethod
    def has_age(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eats_what_food(self):
        pass

    @abstractmethod
    def moves_how(self):
        pass
