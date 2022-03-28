from pendulum import Pendulum, np
import pytest
import numpy as np

#Exercise 2b)
def test_pendulum_call():
    exp_omega = -1.816666666666667 #regnet ut 
    tol = 1e-14

    exp_theta = 0.15
    pendulum_func = Pendulum(L = 2.7)
    dtheta_dt, domega_dt = pendulum_func(0, (np.pi/6, 0.15))
    assert abs(domega_dt - exp_omega) < tol 
    assert abs(dtheta_dt - exp_theta) < tol 

#Exercise 2e)
def test_pendulum_solve():
    obj = Pendulum()
    with pytest.raises(AttributeError):
        obj.theta
        obj.t
        obj.omega

def test_pendulum_initial():
    tol = 1e-14
    obj = Pendulum()
    y0 = (0,0)
    dt = 1 
    T = 10
    obj.solve(y0, T, dt)
    expected_t_values = [i * dt for i in range(T+dt)]
    assert np.all(abs(obj.t - expected_t_values) < tol)
    assert np.sum(obj.theta) == 0
    assert np.sum(obj.omega) == 0
    

'''
pytest -v test_pendulum.py

collected 3 items

test_pendulum.py::test_pendulum_call PASSED                              [ 33%]
test_pendulum.py::test_pendulum_solve PASSED                             [ 66%]
test_pendulum.py::test_pendulum_initial PASSED                           [100%]

'''

