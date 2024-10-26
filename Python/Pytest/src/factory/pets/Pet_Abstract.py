from abc import ABC, abstractmethod


class PetAbstract(ABC):

    @abstractmethod
    def makes_what_sound(self):
        pass

    @abstractmethod
    def eats_what_food(self):
        pass

    @abstractmethod
    def moves_how(self):
        pass
