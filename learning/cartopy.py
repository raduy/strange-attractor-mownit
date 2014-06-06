#!/usr/bin/env python
from numpy.ma import sqrt
import matplotlib

from mpl_toolkits.mplot3d import Axes3D
from learning import attractor


matplotlib.use('TkAgg')

from numpy import arange, sin, zeros, meshgrid
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mpl_toolkits.mplot3d.axes3d as p3

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

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


def lorenz_step(x0, y0, z0, dt):
    a = 5.2
    b = 15.0
    c = 1.0
    #
    xp = (a * (y0 - x0))
    yp = (b * x0 - y0 - z0 * x0)
    zp = (x0 * y0 - c * z0)
    #
    return [x0 + xp * dt, y0 + yp * dt, z0 + zp * dt]


####################
#  Main Loop
####################


for i in range(1, s):
    f = lorenz_step(x_p[i - 1], y_p[i - 1], z_p[i - 1], delta_t)
    x_p[i] = f[0]
    y_p[i] = f[1]
    z_p[i] = f[2]


####################
# Plot
#fig = p.figure()
#ax = p3.Axes3D(fig)
#
#ax.plot3D(x_p, y_p, z_p)
#ax.set_xlabel('X label')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#fig.add_axes(ax)
#p.show()


def destroy():
    sys.exit()


root = Tk.Tk()
root.wm_title("Embedding in TK")
#root.bind("<Destroy>", destroy)


f = Figure(figsize=(16, 9), dpi=100)

ax = f.add_subplot(1, 1, 1, projection='3d')
ax.mouse_init()
X = arange(-5, 5, 0.25)
xlen = len(X)
Y = arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = meshgrid(X, Y)
R = sqrt(X ** 2 + Y ** 2)
Z = sin(R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                       linewidth=0, antialiased=True)

#ax.set_zlim3d(-1, 1)
ax.mouse_init()

#plt.show()

#former


#a = f.add_subplot(1, 1, 1, projection='3d')
#t = arange(0.0, 3.0, 0.01)
#s = sin(2 * pi * t)
#
#
#a.plot3D(x_p, y_p, z_p)
#a.set_xlabel('X label')
#a.set_ylabel('Y')
#a.set_zlabel('Z')

#end former code


#fig.add_axes(ax)
#p.show()
#
#a.plot(t, s)
#a.set_title('Tk embedding')
#a.set_xlabel('X axis label')
#a.set_ylabel('Y label')


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=root, text='Quit', command=destroy)
button.pack(side=Tk.BOTTOM)


def my_print():
    attractor.showcase(10., 2.667, 10.)


up_button = Tk.Button(master=root, text='Up', command=my_print)
up_button.pack(side=Tk.BOTTOM)

input = Tk.Entry(master=root)


def evaluate():
    print "bind"


input.bind("<Return>", evaluate)
input.pack(side=Tk.BOTTOM)

clear_button = Tk.Button(master=root, text='Clear', command=attractor.refresh)
clear_button.pack(side=Tk.BOTTOM)


Tk.mainloop()