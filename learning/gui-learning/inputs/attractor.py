__author__ = 'raduy'

from numpy import *
import pylab as p
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# dx/dt = a(y-x)       == xp
# dy/dt = bx - y - zx  == yp
# dz/dt = xy - cz      == zp


####################
#  Global vars
####################
s = 10000
delta_t = 1e-2


#plot variables
x_p = zeros(s)
y_p = zeros(s)
z_p = zeros(s)

x_p[0] = 30
y_p[0] = 1.
z_p[0] = 10

####################
#  Functions
####################


def lorenz_step(a, b, c, x0, y0, z0, dt):
    #
    xp = (a * (y0 - x0))
    yp = (b * x0 - y0 - z0 * x0)
    zp = (x0 * y0 - c * z0)
    #
    return [x0 + xp * dt, y0 + yp * dt, z0 + zp * dt]


def showcase(a, b, c):
    ####################
    #  Main Loop
    ####################

    #plt.ion()
    for i in range(1, s):
        f = lorenz_step(a, b, c, x_p[i - 1], y_p[i - 1], z_p[i - 1], delta_t)
        x_p[i] = f[0]
        y_p[i] = f[1]
        z_p[i] = f[2]

    ####################
    # Plot
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    ax.plot3D(x_p, y_p, z_p)
    ax.set_xlabel('X label')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    fig.add_axes(ax)
    p.show()


def refresh():
    p.close()
    print "delay"
    showcase(10., 2.6, 10.)

#showcase(10., 2.667, 15.)
