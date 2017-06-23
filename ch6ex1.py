from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  # <- Important
from numpy import pi, arange, sin, cos

dphi=pi/100 # set the spacing in azimuthal angle

N=30 # set the number of azimuthal trips
phi=arange(0,N * 2 * pi, dphi)

theta=phi/N/2 # go from north to south once

r=1  # sphere of radius 1

# convert spherical to Cartesian
x=r*sin(theta)*cos(phi)
y=r*sin(theta)*sin(phi)
z=r*cos(theta)

# plot the spiral
fig = pyplot.figure()
fig.gca(projection='3d')  # Create 3D axis
pyplot.plot(x,y,z)
pyplot.axis('equal')
pyplot.show()
