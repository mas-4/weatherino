from weatherino.core import add
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
    (4, 5, 9),
    (5, 6, 11),
    (6, 7, 13),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
