from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

#Exercise 1a) 
class ExponentialDecay:
    def __init__(self, a):
        if a < 0:
            raise ValueError('a cannot be negative')
        elif a > 0:
            self.a = a

#Exercise 1b) 
    def __call__(self, t, u):
        a = self.a
        dudt = -a*u #RHS
        return dudt

#Exercise 1c)
    def solve(self, u0, T, dt):
        sol = solve_ivp(ExponentialDecay(self.a), [0, T], [u0], t_eval=np.linspace(0, T, T//dt))
        return sol.t, sol.y[0]
        
if __name__ == "__main__":
    a = 0.4
    u0 = 2
    T = 10
    dt = 1
    decay_model = ExponentialDecay(a)
    t, u = decay_model.solve(u0, T, dt)

    plt.plot(t, u)
    plt.show()

