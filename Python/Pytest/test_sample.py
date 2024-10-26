import pytest


def increment_func(x):
    return x+1


@pytest.mark.parametrize("sample_value",list(range(10)))
def test_answer(sample_value):
    assert increment_func(sample_value) == sample_value+1
