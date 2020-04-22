import numpy as np
import matplotlib.pyplot as plt

def condinx(xx):
    u0 = np.sin(xx)

    return u0

def condinv(xx):
    v = 0

    return v

def main():

    # Declaring variables
    dx = 0.1 # Variation of x (m)
    dt = 0.1 # Variation of t (s)

    v = 1 # Speed
    L = 20 # String length (m)
    p = 30 # Final time (s)

    m = int(L/dx+1) # Number of spatial nodes
    n = int(p/dt+1) # Number of temporal nodes

    c = (v**2)*(dt**2)/(dx**2) # if c>1, instability of simulation occurs 

    u = np.zeros((m, n)) # Allocating memory space in variable (Wave amplitude)

    x = np.arange(0, L+dx, dx) # 
    t = np.arange(0, p+dt, dt)

    # Initial condition:
    # How the string was when it started to be observed

    for i in range(m):
        if(x[i]<=np.pi):
            u[i, 0] = condinx(x[i])
        else:
            u[i, 0] = 0

    # Velocity initial condition (du/dt = v)
    for i in range(1, m - 1):
        u[i, 1] = u[i, 0] + n * condinv(x[i]) + (c / 2)*(u[i + 1, 0] - 2 * u[i, 0] + u[i - 1, 0])

    ''' 
    Through Finite Volume Method (FVM), it's possible to obtain the following equation
    to approximate a one-dimensional wave
    '''
    s = 2 * c + 2
    a = c - 1
    b = 2 * c + 2
    e = 4 * c - 4

    for j in range(1, n - 1):
        for it in range(0, 10):
            for i in range(1, m - 1):
                aa = u[i + 1, j + 1] + u[i - 1, j + 1]
                bb = u[i + 1, j] + u[i - 1, j]
                aaa = u[i + 1, j - 1] + u[i - 1, j - 1]

                u[i, j + 1] = (a*aa + b * bb - e * u[i, j] + a * aaa - s * u[i, j - 1]) / s


    # To obtain animated plot:
    for j in range(1, n):
        plt.figure("one-dimensional Wave")

        plt.axes(xlim=(0, 20), ylim=(-1, 1))

        plt.plot(x[:], u[:, j-1])
        plt.grid(True)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

if __name__=="__main__":
    main()
