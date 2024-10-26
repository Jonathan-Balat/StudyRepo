import pytest
from src.factory.Pet_Factory_Class import PetFactory


NAME:  str  = 'Doug'
AGE:   int  = 3
SOUND: str  = "Barks"
MOVES: list = ["Runs", "Walks"]
EATS:  str  = "Dog food"


@pytest.fixture
def dog():
    return PetFactory.adopt_pet('dog', NAME, AGE)


def test_class_instantiation(dog):
    assert dog is not None


def test_dog_name_attr(dog):
    assert dog.has_name() == NAME


def test_dog_age_attr(dog):
    assert dog.has_age() == AGE


def test_dog_sound_attr(dog):
    assert dog.make_sound() == SOUND


def test_dog_eat_attr(dog):
    assert dog.eats_what_food() == EATS


def test_dog_move_attr(dog):
    assert dog.moves_how() == MOVES
