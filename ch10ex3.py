from numpy import arange, cos,sin

N=1000
a=0
b=5.
dx=(b-a)/N

x=arange(.5*dx,b - 0.5 * dx, dx)  # build an x array of centered values
f=cos(x)  # load the function

# do the approximate integral
s=sum(f)*dx

# compare with the exact answer, which is sin(5)
err=s-sin(5)
print(err)
