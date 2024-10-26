import pytest
from src.Math_Class import MathClass

FIBO_SAMPLE_DATA = [(0, 0), (1, 1), (2, 1), (10, 55), (12, 144), (19, 4181), (20, 6765), (30, 832040)]
@pytest.fixture
def MClass():
    return MathClass()


def test_class_instantiation(MClass):
    assert MClass is not None


@pytest.mark.parametrize("test_num, test_val", FIBO_SAMPLE_DATA)
def test_class_fibo(MClass, test_num, test_val):
    assert MClass.fibbonacci_sequence_prototype(test_num) == test_val


@pytest.mark.parametrize("test_num, test_val", FIBO_SAMPLE_DATA)
def test_class_fibo_improved(MClass, test_num, test_val):
    assert MClass.fibbonacci_sequence_lru(test_num) == test_val


