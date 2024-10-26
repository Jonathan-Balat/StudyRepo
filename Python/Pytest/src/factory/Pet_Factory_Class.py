from src.factory.pets.Pet_Dog import PetDog
from random import choice, randint

__all__ = ['PetFactory']


class PetFactory:

    PET_TYPES = {'dog': PetDog}

    DOG_NAMES = ['Arby', 'Butch', 'Cookie', 'Doug']
    DOG_NAMES_TAKEN = []

    @classmethod
    def adopt_pet(cls, pet_type, name=None, age=None):
        pet_type = pet_type.lower()

        if pet_type not in list(cls.PET_TYPES.keys()):
            pet = None
            print(f"{pet_type} is an invalid pet type")

        else:  # Dog case

            if name is None:
                name = choice(cls.DOG_NAMES)
            if age is None:
                age = randint(1, 10)

            pet = cls.PET_TYPES[pet_type](name, age)

        return pet

    @classmethod
    def bestow_pet(cls, pet_obj):

        if isinstance(pet_obj, PetDog):
            name = pet_obj.has_name()

            if name in cls.DOG_NAMES_TAKEN:
                cls.DOG_NAMES_TAKEN.pop(name)
                cls.DOG_NAMES.append(name)
            else:
                print(f"{name} seem to be new here")
                cls.DOG_NAMES.append(name)
        else:
            print("Wrong Pet")
