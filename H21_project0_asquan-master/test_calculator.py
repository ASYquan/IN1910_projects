from calculator import add, divide, factorial, sin, pi, sqrt
import pytest

def test_add():
    tol = 1e-10
    exp = 0.3
    assert abs(add(0.1,0.2)-exp) < tol


def test_divide():
    tol = 1e-10
    exp_val = [3, 2.25, 0.5, 3.5]
    x_val = [6, 9, 1, 7]
    y_val = [2, 4, 2, 2]
    for x, y, exp in zip(x_val, y_val, exp_val):
        assert abs(divide(x,y)-exp) < tol, f'Failed for x = {x}, y = {y}, expcted {exp}, got {divide(x,y)}, tolerance = {tol}'


def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(0) == 1 


def test_sin():
    tol = 1e-10
    x_val   = [0,(pi/4), (pi/2),3*(pi/2)]
    exp_val = [0, 1/sqrt(2), 1, -1]
    for x, exp in zip(x_val, exp_val):
        assert abs(sin(x)-exp) < tol

def test_factorial_raises_ValueError_for_negatives():
    try:
        factorial(-1)
    except ValueError:
        # Correct exception is raised, test should pass
        pass
    except Exception:
        # This catches any other type of exception, test should fail
        raise Exception
    else:
        # No exception has been raised, test should fail
        raise Exception

def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_raises_TypeError_for_floats():
    with pytest.raises(TypeError):
        factorial(1/3)

def test_divide_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        divide(3/0)
