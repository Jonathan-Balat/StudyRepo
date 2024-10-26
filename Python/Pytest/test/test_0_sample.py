import pytest


def decrement_func(x):
    return x-1


@pytest.mark.parametrize("sample_value", list(range(10)))
def test_0_answer(sample_value):
    assert decrement_func(sample_value) == sample_value
