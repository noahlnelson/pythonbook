from numpy import arange, mgrid,ones,array
from matplotlib import pyplot
x = arange(0,1,0.1)
y = arange(0,1,0.1)

#Define the position arrays x and y
X,Y = meshgrid(x,y)
#X,Y = mgrid[0:1:0.1,0:1:0.1]  #This won't work for streamplots.!!!

#Define the flow velocity arrays u and v
u = X
v = -Y

#Create a quiver plot of the flow velocity
pyplot.figure()
#pyplot.quiver(X,Y,u,v)

#Plot streamlines that start at different points along the line y=1.
startx = arange(0.05,0.95,0.05)
starty = ones(len(startx)) -0.2
sp = array([startx,starty])
pyplot.streamplot(x,y,u,v,start_points=sp.T,color='crimson',linewidth = 2)
pyplot.show()
