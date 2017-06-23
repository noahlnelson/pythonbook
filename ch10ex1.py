from numpy import arange, sin, cos, zeros_like
from matplotlib import pyplot

dx=1./1000
x=arange(0,4,dx)
N=len(x)
f=sin(x)

# Do the derivative at the interior points all at once using
# the colon command

dfdx = zeros_like(f)  # Create array of zeros.
dfdx[1:N-1]=(f[2:N]-f[0:N-2])/(2*dx)  # Populate array with derivative values

# linearly extrapolate to the end points
dfdx[0]=2*dfdx[1]-dfdx[2]
dfdx[N-1]=2*dfdx[N-2]-dfdx[N-3]

# now plot both the approximate derivative and the exact
# derivative cos(x) to see how well we did
pyplot.plot(x,dfdx,'r-',x,cos(x),'b-')

# also plot the difference between the approximate and exact
pyplot.figure()
pyplot.plot(x,dfdx-cos(x),'b-')
pyplot.title('Difference between approximate and exact derivatives')
pyplot.show()
