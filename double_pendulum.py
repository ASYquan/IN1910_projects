from math import degrees
import numpy as np 
from scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



#Exercise 3a)

class DoublePendulum:
    def __init__(self, L1 = 1, L2 = 1, g = 9.81):
        self.M1 = 1
        self.M2 = 1

        self.L1 = L1
        self.L2 = L2
        self.g = g

    def __call__(self, t, y):
        L1 = self.L1; L2 = self.L2; g = self.g
        theta1, omega1, theta2, omega2 = y
        dtheta = theta2-theta1
        
        domega1_dt = ((L1 * (omega1**2)*np.sin(dtheta)*np.cos(dtheta)
                        + g*np.sin(theta2) * np.cos(dtheta)
                        + L2*(omega2**2) * np.sin(dtheta) - 2*g*np.sin(theta1)) 
                        /(2*L1 - L1*(np.cos(dtheta))**2))

        domega2_dt = ((-L2 * (omega2**2)*np.sin(dtheta)*np.cos(dtheta)
                        + 2*g*np.sin(theta1) * np.cos(dtheta)
                        - 2*L1*(omega1**2) * np.sin(dtheta) - 2*g*np.sin(theta2)) 
                        /(2*L2 - L2*(np.cos(dtheta))**2))

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        return dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt
    
    
#Exercise 3c)

    def solve(self, y0, T, dt, angle = 'rad'):
        if angle == 'deg':
            y0 = np.radians(y0)
        self.y0 = y0
        self.T  = T
        self.dt = dt
        dp = DoublePendulum()
        sol = solve_ivp(self, [0, T], self.y0, t_eval=np.linspace(0, T, int(T/dt)+1), method = 'Radau')
        self._theta1    = sol.y[0]
        self._theta2    = sol.y[2] 
        self._t         = sol.t

#Exercise 3d)
    @property
    def theta1(self):
        
        if not hasattr(self, '_theta1'):
            raise AttributeError('solve-method has not been called')
        
        return self._theta1

    @property 
    def theta2(self):
        
        if not hasattr(self, '_theta2'):
            raise AttributeError('solve-method has not been called')
        
        return self._theta2

    @property
    def t(self):

        if not hasattr(self, '_t'):
            raise AttributeError('solve-method has not been called')
        
        return self._t

    @property
    def x1(self):
        self._x1 = self.L1*np.sin(self.theta1)
        
        return self._x1

    @property
    def y1(self):
        self._y1 = -self.L1*np.cos(self.theta1)
        
        return self._y1

    @property 
    def x2(self):
        self._x2 =  self.x1 + self.L2*np.sin(self.theta2)
        
        return self._x2
    
    @property 
    def y2(self):
        self._y2 =  self.y1 - self.L2*np.cos(self.theta2)
        
        return self._y2

#Exercise 3e) 
    @property
    def potential(self):
        
        if not hasattr(self, '_y1'):
            raise AttributeError('y1 has not been calculated, use solve-method')

        
        if not hasattr(self, '_y2'):
            raise AttributeError('y2 has not been calculated, use solve-method')
        
        M1 = self.M1; M2 = self.M2
        P1 = M1*self.g*(self.y1 + self.L1)
        P2 = M2*self.g*(self.y2 + self.L1 + self.L2)
        self._P = P1 + P2
        
        return self._P
        
    @property 
    def vx1(self):
        self._vx1 = np.gradient(self.x1, self.dt)

        return self._vx1

    @property
    def vy1(self):
        self._vy1 = np.gradient(self.y1, self.dt)

        return self._vy1

    @property
    def vx2(self):
        self._vx2 = np.gradient(self.x2, self.dt)

        return self._vx2

    @property
    def vy2(self):
        self._vy2 = np.gradient(self.y2, self.dt)

        return self._vy2

    @property 
    def kinetic(self):
        K1 = (1/2) * self.M1 * ((self.vx1**2) + (self.vy1**2))
        K2 = (1/2) * self.M2 * ((self.vx2**2) + (self.vy2**2))
        self._K = K1 + K2

        return self._K


#Part4

#Exercise 4a)

    def create_animation(self):
        fig = plt.figure()
        
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))
        
        self.pendulums, = plt.plot([], [], 'o-', lw=2)
        self.animation = FuncAnimation(fig,
                                             self._next_frame,
                                             frames=range(len(self.x1)), 
                                             repeat=None,
                                             interval=1000*self.dt, 
                                             blit=True)

    def _next_frame(self, i):
        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        
        return self.pendulums,

#Exercise 4b)

    def show_animation(self):
        plt.show()

    def save_animation(self, filename):

        if not isinstance(filename, str):
            raise TypeError('Filename must be a string')
        
        self.animation.save(filename, fps=60)
        
        

if __name__ == '__main__':
#Exercise 3e)
    y0 = (3*np.pi/7, 0, 3*np.pi/4, 0)
    T = 6
    dt = 0.01
    obj = DoublePendulum()
    obj.solve(y0,T,dt)
    total = obj.kinetic + obj.potential
    plt.plot(obj.t, obj.kinetic, label = 'Kinetic')
    plt.plot(obj.t, obj.potential, label = 'Potential')
    plt.plot(obj.t, total, label = 'Total energy' )
    plt.legend()
#Part 4
    obj.create_animation()
    obj.show_animation()
    obj.save_animation('example_simulation.mp4') 
        
'''
python3 double_pendulum.py

'''
