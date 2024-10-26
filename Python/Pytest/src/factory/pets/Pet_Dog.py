from .Pet_Abstract import PetAbstract


# This limits what content can be imported from this file.
__all__ = ['PetDog']


class PetDog(PetAbstract):

    def __init__(self, name: str, age: int):
        super().__init__()

        self.__name = name
        self.__age = age
        self.__sound = "Barks"
        self.__moves = ["Runs", "Walks"]
        self.__eats = "Dog food"

    def has_name(self):
        return self.__name

    def has_age(self):
        return self.__age

    def make_sound(self):
        return self.__sound

    def eats_what_food(self):
        return self.__eats

    def moves_how(self):
        return self.__moves
