#Calculates GCD of two integers a,b
import math

list = []
steps = []

def calc_gcd(l):
    if l[1] > l[0]:
        return -1
    else:
        return gcd(l[0],l[1])

#a/b or b | a
def _gcd(a,b):

    steps.append("%5d = %5d * %5d + %5d" % (a, math.floor(a/b), b, a%b))
    list.append([a,math.floor(a/b),b,a%b])

    if a%b != 0:
        return gcd(b,a%b)

    return b

def gcd(a,b):

    return(_gcd(a,b))
