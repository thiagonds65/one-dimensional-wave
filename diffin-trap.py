import numpy as np
import matplotlib.pyplot as plt

def condinx(xx):
    u0 = np.sin(xx)

    return u0

def condinv(xx):
    v = 0

    return v


dx = 0.1
dt = 0.1

v = 1
L = 20
p = 30

m = int(L/dx+1)
n = int(p/dt+1)

c = (v**2)*(dt**2)/(dx**2)

u = np.zeros((m, n))
uu = np.zeros((m, n))

x = np.arange(0, L+dx, dx)
t = np.arange(0, p+dt, dt)

for i in range(m):
    if(x[i]<=np.pi):
        u[i, 0] = condinx(x[i])
    else:
        u[i, 0] = 0

for i in range(1, m - 1):
    u[i, 1] = u[i, 0] + n * condinv(x[i]) + (c / 2)*(u[i + 1, 0] - 2 * u[i, 0] + u[i - 1, 0])

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


for j in range(1, n):
    plt.figure("one-dimensional Wave")

    plt.plot(x[:], u[:, j-1])
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

