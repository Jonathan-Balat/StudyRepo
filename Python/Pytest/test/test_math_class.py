import pytest
import logging
from src.Math_Class import MathClass


def test_class_instantiation():
    MC = MathClass()

    assert MC is not None


@pytest.mark.parametrize("test_num, test_val", [(0,0), (1,1), (2,1), (12, 144)])
def test_class_fibo(test_num, test_val):
    MC = MathClass()

    assert MC.fibbonacci_sequence(test_num) == test_val


