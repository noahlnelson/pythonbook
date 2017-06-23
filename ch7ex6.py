from numpy import arange,sin,cos
from matplotlib import pyplot

t = 0
x = arange(0,5,0.01)   #Domain over which I want to plot the function.
 while t < 10:
    y = sin(5 * x - 3 * t) * cos(2 * x)  #Construct array of function
                                         # values at current time.
    pyplot.clf()  # Clear the canvas, otherwise all plots end up on
                  # top of each other
    pyplot.plot(x,y,'r-',linewidth=3)
    pyplot.xlabel('x')
    pyplot.ylabel('f(x)')
    pyplot.title('t = {:.4f}'.format(t))
    pyplot.draw()           # draw the plot, but don't wait for
                            # someone to close the window.
    pyplot.pause(0.01)      # Wait before plotting the next one.
    t = t + .1              # Advance time.
