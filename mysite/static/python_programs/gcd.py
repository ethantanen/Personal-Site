#Calculates GCD of two integers a,b

import math

list = [] #list for print out
steps = [] #list for step by step data

#a/b or b | a
def _gcd(a,b):

    # Nicely formatted printable
    steps.append("%5d = %5d * %5d + %5d" % (a, math.floor(a/b), b, a%b))
    
    # Data from each step in convenient data structure
    list.append([a,math.floor(a/b),b,a%b])

    # Continue algorithm until b divides a
    if a%b != 0:
        return _gcd(b,a%b)

    # Return gcd
    return b

# Make sure smaller number is first parameter
def gcd(a,b):

    if a > b:
        return _gcd(b,a)
    else:
        return _gcd(a,b)
