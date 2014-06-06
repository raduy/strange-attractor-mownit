import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorentz attractor showcase

# dx/dt = a(y - x)
# dy/dt = cx - y - xz
# dz/dt = xy - bz


def lorenz(x, y, z, a=10., b=2.667, c=30):
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


def showcase(a=10., b=2.667, c=10):
    # Stepping through "time".
    for i in range(stepCnt):
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], a, b, c)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    fig = plt.figure(figsize=(16, 12), dpi=100, facecolor='k', edgecolor='k')
    ax = fig.gca(projection='3d')
    fig.canvas.set_window_title("Strange Attractor Showcase, Mownit 2014, Lukasz Raduj")

    ax.plot(xs, ys, zs, color='red')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor Showcase (use mouse to move)")

    plt.show()


def refresh():
    plt.close()
    print "delay"
    showcase()

if __name__ == '__main__':
    showcase()


