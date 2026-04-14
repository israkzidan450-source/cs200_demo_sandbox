import main
import pytest


def test_foo():
    assert main.foo(0, 0) == 1
    assert main.foo(5, 0) == 1
    assert main.foo(0, 5) == 1
    assert main.foo(5, 5) == 26

@pytest.mark.parametrize(
    ("input_x, input_y, expected"),
    (
        (0, 0, 0),
        (5, 0, 0),
        (0, 5, -1),
        (5, 5, 3124)
    )
)
def test_bar(input_x, input_y, expected):
    assert main.bar(input_x, input_y) == expected