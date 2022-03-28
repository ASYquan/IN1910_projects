import pytest
from calculator import factorial, divide, sin, pi, sqrt

@pytest.mark.parametrize(
    "arg, output", [(1, 1), (2, 2), (3, 6), (5, 120), (0, 1)]
)
def test_factorial(arg, output):
    assert factorial(arg) == output

@pytest.mark.parametrize(
    "x, y, output", [(1, 4, 0.25), (2, 1, 2), (6, 3, 2), (16, 4, 4), (1, 1, 1)]
)

def test_divide(x, y, output):
    tol = 1e-10
    assert abs(divide(x,y)-output) < tol

@pytest.mark.parametrize(
    "x, output", [(0, 0), (pi/4, 1/sqrt(2)), (pi/2, 1), (3*(pi/2), -1), (pi/3, sqrt(3)/2)]
)

def test_sin(x, output):
    tol = 1e-10
    assert abs(sin(x) - output) < tol
