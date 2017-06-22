from numpy import arange, meshgrid,sqrt,log
from matplotlib import pyplot
x = arange(-5.25,5.25,0.5) # define the x and y grids (avoid (0,0))
y = arange(-5.25,5.25,0.5) # define the x and y grids (avoid (0,0))

X,Y=meshgrid(x,y)

# Electric field of a long charged wire
Ex=X/(X**2+Y**2)
Ey=Y/(X**2+Y**2)

pyplot.quiver(X,Y,Ex,Ey) # make the field arrow plot
pyplot.title('E of a long charged wire')
pyplot.axis('equal')  # make the x and y axes be equally scaled

# Magnetic field of a long current-carrying wire
Bx=-Y/(X**2+Y**2)
By=X/(X**2+Y**2)

# make the field arrow plot
pyplot.figure()
pyplot.quiver(X,Y,Bx,By)
pyplot.axis('equal')  # make the x and y axes be equally scaled
pyplot.title('B of a long current-carrying wire')

# The big magnitude difference across the region makes most arrows too small
# to see.  This can be fixed by plotting unit vectors instead
# (losing all magnitude information, but keeping direction)
B=sqrt(Bx**2+By**2)
Ux=Bx/B
Uy=By/B

pyplot.figure()
pyplot.quiver(X,Y,Ux,Uy);
pyplot.axis('equal')  # make the x and y axes be equally scaled
pyplot.title('B(wire): unit vectors')

# Or, you can still see qualitative size information without such a big
# variation in arrow size by having the arrow length be logarithmic.
Bmin=B.min()
Bmax=B.max()
# s is the desired ratio between the longest arrow and the shortest one
s=2  # choose an arrow length ratio
k=(Bmax/Bmin)**(1/(s-1))
logsize=log(k*B/Bmin)
Lx=Ux*logsize
Ly=Uy*logsize

pyplot.figure()
pyplot.quiver(X,Y,Lx,Ly)
pyplot.axis('equal')  # make the x and y axes be equally scaled
pyplot.title('B(wire): logarithmic arrows')
pyplot.show()
