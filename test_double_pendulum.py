from double_pendulum import DoublePendulum
import pytest
import numpy as np

#Exercise 3b)
@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (  0,   0,            0),
        (  0, 0.5,  3.386187037), 
        (0.5,   0, -7.678514423),
        (0.5, 0.5, -4.703164534),
    ]
)
def test_domega1_dt(theta1, theta2, expected):
    dp = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    dtheta1_dt, domega1_dt, _, _ = dp(t, y)
    assert np.isclose(dtheta1_dt, 0.25)
    assert np.isclose(domega1_dt, expected)
    
@pytest.mark.parametrize(
    "theta1, theta2, expected",
    [
        (  0,   0,          0.0),
        (  0, 0.5, -7.704787325),
        (0.5,   0,  6.768494455),
        (0.5, 0.5,          0.0),
    ],
)
def test_domega2_dt(theta1, theta2, expected):
    dp = DoublePendulum()
    t = 0
    y = (theta1, 0.25, theta2, 0.15)
    _, _, dtheta2_dt, domega2_dt = dp(t, y)
    assert np.isclose(dtheta2_dt, 0.15)
    assert np.isclose(domega2_dt, expected)

#Exercise 3f):

#Unit-test: 1
def test_DoublePendulum_solve_raise_exception():
    
    ''' Tester om feilmelding kommer, før solve-metoden blir kalt'''

    obj = DoublePendulum()
    with pytest.raises(AttributeError):
        obj.theta1
        obj.theta2
        obj.omega1
        obj.omega2
        obj.t

#Unit-test: 2
def test_DoublePendulum_initial():

    ''' Sjekker om alle t-verdier er like, og sjekker om dobbel pendulum ligger i ro for y0 = (0,0,0,0) '''

    tol = 1e-14
    y0 = (0, 0, 0, 0)
    T = 30
    dt = 1
    obj = DoublePendulum()
    obj.solve(y0, T, dt)
    expected_t_values = [i * dt for i in range(int(T+dt))]
    assert np.all(abs(obj.t- expected_t_values) < tol)
    assert np.sum(obj.theta1) == 0
    assert np.sum(obj.theta2) == 0

#Unit-test: 3
def test_DoublePendulum_potential_raise_exception():

    ''' Tester om potensialenergi gir feilmelding når y1 og y2 mangler''' 

    obj = DoublePendulum()
    with pytest.raises(AttributeError):
        obj.potential

'''
pytest -v test_double_pendulum.py

collected 11 items

test_double_pendulum.py::test_domega1_dt[0-0-0] PASSED                   [  9%]
test_double_pendulum.py::test_domega1_dt[0-0.5-3.386187037] PASSED       [ 18%]
test_double_pendulum.py::test_domega1_dt[0.5-0--7.678514423] PASSED      [ 27%]
test_double_pendulum.py::test_domega1_dt[0.5-0.5--4.703164534] PASSED    [ 36%]
test_double_pendulum.py::test_domega2_dt[0-0-0.0] PASSED                 [ 45%]
test_double_pendulum.py::test_domega2_dt[0-0.5--7.704787325] PASSED      [ 54%]
test_double_pendulum.py::test_domega2_dt[0.5-0-6.768494455] PASSED       [ 63%]
test_double_pendulum.py::test_domega2_dt[0.5-0.5-0.0] PASSED             [ 72%]
test_double_pendulum.py::test_DoublePendulum_solve_raise_exception PASSED [ 81%]
test_double_pendulum.py::test_DoublePendulum_initial PASSED              [ 90%]
test_double_pendulum.py::test_DoublePendulum_potential_raise_exception PASSED [100%]
'''
