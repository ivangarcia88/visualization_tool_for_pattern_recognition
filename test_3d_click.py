import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D, proj3d
import numpy as np
import matplotlib.pyplot as plt
 
def format_coord(event,ax):
    # nearest edge
    self = ax
    xd = event.xdata
    yd = event.ydata
    p0, p1 = min(self.tunit_edges(),
                 key=lambda edge: proj3d._line2d_seg_dist(
                     edge[0], edge[1], (xd, yd)))
 
    # scale the z value to match
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    d0 = np.hypot(x0-xd, y0-yd)
    d1 = np.hypot(x1-xd, y1-yd)
    dt = d0+d1
    z = d1/dt * z0 + d0/dt * z1 
    x, y, z = proj3d.inv_transform(xd, yd, z, self.M)
    xs = self.format_xdata(x)
    ys = self.format_ydata(y)
    zs = self.format_zdata(z)
    print('x=%s, y=%s, z=%s' % (xs, ys, zs))
    return (xs, ys, zs)
 
fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.scatter(x, y, z, label='parametric curve')
ax.legend()
 
#fig.canvas.mpl_connect('button_press_event', lambda event: vp.click2D(event, window, neigh, classes, limg))
fig.canvas.mpl_connect('button_press_event', lambda event: format_coord(event, ax))
#fig.canvas.mpl_connect( 'button_press_event', demo_format_coord )
 
plt.show()