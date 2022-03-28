from exp_decay import ExponentialDecay
import numpy as np
import matplotlib.pyplot as plt 

#Exercise 1b)
def test_exp_decay():
    tol = 1e-14
    exp = -1.28
    func = ExponentialDecay(0.4)
    assert abs(func(1, 3.2)-exp) < tol

#Exercise 1d) 

def test_exp_decay_solve(): 
    '''
Testen sammenligner tidspunkt og løsnings-punkt fra den eksakte-
og numeriske løsningen.
''' 
    a   = 0.4; u0 = 2; T = 10
    dt  = 1
    t = np.linspace(0,T, dt) #Tidspunkt for eksakte løsning 
    tol = 1e-14 
    decay_model = ExponentialDecay(a)
    t_arr, u_arr = decay_model.solve(u0, T, dt)
    exac    = u0*np.exp(-a*t) # Den eksakte løsningen
    #Test for løsnings-punkt
    for u_val1, u_val2  in zip(u_arr, exac):
        assert abs(u_val1-u_val2) < tol
    #Test for tidspunkt
    for t_val1, t_val2 in zip(t_arr, t):
        assert t_val1==t_val2

'''
pytest -v test_exp_decay.pytest

collected 2 items

test_exp_decay.py::test_exp_decay PASSED                                 [ 50%]
test_exp_decay.py::test_exp_decay_solve PASSED                           [100%]
'''
