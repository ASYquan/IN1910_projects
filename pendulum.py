from math import degrees
from matplotlib import colors
import numpy as np 
from scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt 

#Exercise 2a)
class Pendulum:
    def __init__(self, L = 1, M = 1 ,g = 9.81):
        self.L = L
        self.M = M
        self.g = g

    def __str__(self): 
        L = self.L; M = self.M; g = self.g
        return f'{L}, {M}, {g}'

    def __call__(self, t, y):
        L = self.L; g = self.g
        theta, omega     = y 
        dtheta_dt        = omega
        domega_dt        = -g/L*np.sin(theta) 
        return dtheta_dt, domega_dt
    
    #Exercise 2c)
    def solve(self, y0, T, dt, angle = "rad"):
        self.T = T
        self.y0 = y0
        self.dt = dt
        if angle == "deg":
            y0[0] = np.radians(y0[0])
        sol = solve_ivp(self, [0, T], y0, t_eval=np.linspace(0, T, int(T/dt)+1))

        #Exercise 2d) 
        self._t     = sol.t
        self._omega = sol.y[1] 
        self._theta = sol.y[0]

    @property
    def theta(self):
        if not hasattr(self, '_theta'): 
            raise AttributeError('Solve-method has not been called')
        
        else:
            return self._theta

    @property 
    def omega(self):
        if not hasattr(self, '_omega'): 
            raise AttributeError('Solve-method has not been called')
        
        else:
            return self._omega

    @property
    def t(self):
        if not hasattr(self, '_t'):
            raise AttributeError('Solve-method has not been called')
        
        else:
            return self._t 


#Exercise 2f)
    @property
    def x(self):
        return self.L * np.sin(self._theta)
    
    @property
    def y(self):
        return -self.L * np.cos(self._theta)


#Exercise 2g)
    @property
    def potential(self):
        return self.M * self.g * (self.y + self.L)
    
    @property
    def vx(self):
        return np.gradient(self.x, self._t)
    
    @property
    def vy(self):
        return np.gradient(self.y, self._t)
    
    @property
    def kinetic(self):
        return 1/2 * self.M * (self.vx**2 + self.vy**2)

#Exercise 2i)
class DampenedPendulum(Pendulum):
    def __init__(self, B, L=1, M=1, g=9.81):
        super().__init__(L, M, g)
        self._B = B

    def __call__(self, t, y):
        theta, omega = y
        dtheta_dt = omega
        domega_dt = ((-self.g / self.L) * np.sin(theta)) - (self._B / self.M) * omega
        return dtheta_dt, domega_dt
    
    @property
    def x(self):
        return self.L * np.sin(self.theta)
    
    @property
    def y(self):
        return -self.L * np.cos(self.theta)

    #Exercise 2h)
if __name__ == '__main__':
    obj = Pendulum()
    obj.solve((np.pi / 3, 0), 5, 0.001)
    plt.title('Pendulum')
    plt.plot(obj.t, obj.kinetic, label='Kinetic energy', color='b')
    plt.plot(obj.t, obj.potential, label='Potential energy', color='r')
    plt.plot(obj.t, obj.theta, label='\u03F4')
    plt.plot(obj.t, obj.kinetic + obj.potential, label='Total energy', color='g')
    plt.legend()
    plt.show()
    #Exercise 2i)
    obj_damp = DampenedPendulum(np.linspace(0, 30, 1))
    obj_damp.solve((np.pi / 3, 0), 30, 0.001)
    plt.title('Dampened pendulum')
    plt.plot(obj_damp.t, obj_damp.potential + obj_damp.kinetic, label='Total energy')
    plt.legend()
    plt.show()

"""
Terminal > Python3 pendulum.py

"""
