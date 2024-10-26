import pytest

from src.Sample_Class import SampleClass


def test_class_instantiation():
    SC = SampleClass()

    assert SC is not None
