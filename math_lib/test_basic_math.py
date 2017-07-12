import pytest

import basic_math


@pytest.fixture(scope="module")
def a():
    return 2


@pytest.fixture(scope="module")
def b():
    return 5


def test_math_add(a, b):
    result = basic_math.math_add(a, b)
    assert result == 7


def test_math_multi(a, b):
    result = basic_math.math_multi(a, b)
    assert result == 10
