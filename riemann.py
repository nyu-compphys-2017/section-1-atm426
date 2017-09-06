# This is a python file! The '#' character indicates that the following line is a comment.

import numpy as np


# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return
    
    
#Implement the Riemann Sum approximation for integrals.

def fn( x ):

    y = x**2.
    return y


def r_mann( a , b , N, fn ):
    """
    a : starting point
    b : ending point
    N : number of rectangles
    fn : input function
    """
    
    width = (b - a) / N
    print width
    x = np.arange(a+width, b+width, width)
    return x
    
    

    
    
    
