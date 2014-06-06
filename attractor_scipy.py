from numpy.ma import sqrt, array
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate

# Lorentz attractor showcase

# dx/dt = a(y - x)
# dy/dt = cx - y - xz
# dz/dt = xy - bz


def draw_plot(xs, ys, zs):
    fig = plt.figure(figsize=(16, 12), dpi=100, facecolor='k', edgecolor='k')
    ax = fig.gca(projection='3d')
    fig.canvas.set_window_title("Strange Attractor Showcase, Mownit 2014, Lukasz Raduj")
    ax.plot(xs, ys, zs, color='red')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor Showcase (use mouse to move)")
    plt.show()


def showcase(a=10., b=2.667, c=10):

    def dX_dt(X, t=0):
        return array([a * (X[1] - X[0]),
                      c * X[0] - X[1] - X[0] * X[2],
                      X[0] * X[1] - b * X[2]])

    # initial value
    X0 = [10., 0.5, 1.]

    t = np.linspace(0, 100, 10000)

    X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)

    print infodict['message']

    xs, ys, zs = X.T
    draw_plot(xs, ys, zs)


if __name__ == '__main__':
    showcase()