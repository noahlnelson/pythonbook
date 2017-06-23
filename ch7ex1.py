from numpy import arange,meshgrid,cos,exp,pi,mgrid
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  #<- You need this to make 3D plots

# Define the arrays x and y
# Don't make the step size too small or you will kill the
# system (you have a large, but finite amount of memory)
x=arange(-1,1,0.1)
y=arange(0,1.5,0.1)

# Use meshgrid to convert these 1-d arrays into 2-d matrices
# of x and y values over the plane
X,Y=meshgrid(x,y)
#X,Y=mgrid[-1:1:0.1,0:1.5:0.1]  # You could also do this in place of meshgrid
# Get F(x,y) by using F(X,Y). Note the use of .* with X and Y
# rather than with x and y
F=(2-cos(pi*X))*exp(Y)

# Plot the function
fig = pyplot.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(X,Y,F)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
