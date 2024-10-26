from Pet_Abstract import PetAbstract


__all__ = ['PetDog']


class PetDog(PetAbstract):

    def __init__(self, name, age):
        super().__init__(name, age)

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
