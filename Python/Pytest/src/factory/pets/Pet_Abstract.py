from abc import ABC, abstractmethod


class PetAbstract(ABC):

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

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
