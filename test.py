theProduct = 1.
term = 1.0  # Load the first term in the sum
s = term  # Initialize the sum 
n = 1     # Set a counter
while term > 1e-10:  # Loop while term is bigger than 1e-10
    n = n + 1        #Add 1 to n so that it will count: 2,3,4,5
    term = 1./n**2    # Calculate the next term to add
    s = s + term     # Add 1/n^2 to the running total
    if n > 50000:
        print 'This is taking too long. I''m outta here...'
        break
print s    

