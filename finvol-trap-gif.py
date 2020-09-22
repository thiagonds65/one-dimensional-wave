import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def condinx(xx):
    u0 = np.sin(xx)

    return u0


def condinv(xx):
    v = 0

    return v

# Declaring variables
dx = 0.1  # Variation of x (m)
dt = 0.1  # Variation of t (s)

v = 1.0  # Speed
L = 20  # String length (m)
p = 40  # Final time (s)

fps = 10 # frame per sec

m = int(L/dx+1)  # Number of spatial nodes
n = int(p/dt+1)  # Number of temporal nodes
frn = n # frame number of the animation

c = (v**2)*(dt**2)/(dx**2)  # if c>1, instability of simulation occurs

# Allocating memory space in variable (Wave amplitude)
u = np.zeros((m, n))

x = np.arange(0, L+dx, dx)
t = np.arange(0, p+dt, dt)

# Initial condition:
# How the string was when it started to be observed

for i in range(m):
    if(x[i] <= np.pi):
        u[i, 0] = condinx(x[i])
    else:
        u[i, 0] = 0

# Velocity initial condition (du/dt = v)
for i in range(1, m - 1):
    u[i, 1] = u[i, 0] + dt * \
        condinv(x[i]) + (c / 2)*(u[i + 1, 0] - 2 * u[i, 0] + u[i - 1, 0])

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

            u[i, j + 1] = (a*aa + b * bb - e * u[i, j] +
                            a * aaa - s * u[i, j - 1]) / s

fig = plt.figure()
ax = plt.axes(xlim=(0, L), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def update_plot(i):
    uarray = u[:, i]
    line.set_data(x, uarray)
    return line,


ani = animation.FuncAnimation(fig, update_plot, init_func=init, frames=frn, interval=20, blit=True)
#ani.save('wave_propagation_1d-teste.gif', writer='imagemagick', fps=fps*3)
#Retirar comentário acima para salvar gif da animação
plt.show()


