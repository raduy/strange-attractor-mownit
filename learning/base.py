import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorentz attractor showcase

# dx/dt = a(y - x)
# dy/dt = cx - y - xz
# dz/dt = xy - bz


def lorenz(x, y, z, a=10, c=30, b=2.667):
    x_dot = a * (y - x)
    y_dot = c * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


dt = 0.01
stepCnt = 10000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

# Setting initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)


def showcase(a, b, c):
    # Stepping through "time".
    for i in range(stepCnt):
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], a, c, b)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(xs, ys, zs)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.show()


def refresh():
    plt.close()
    print "delay"
    showcase(10., 2.6, 10.)

#showcase(10., 2.667, 10.)


