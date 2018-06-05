import math

# Generates the next prime after the input prime
def next_prime(l):
    
    flag = False # Is not prime flag
    
    while True:
        
        l += 1 # Test if the number one higher than the previous is prime
        
        # Divide by every number less than l
        for i in range (2,l):
            
            #If i divides l than l is not prime
            if l%i == 0: flag = True
    
    
        # Return l if that sucker is prime!
        if flag == False: return l
        
        # Reset flag and repeat!
        flag = False

# Factors a number by dividing by progresively larger primes
def factor(a):
    
    factors = {} #Dict to store prime factor and exp/count
    
    p = 2 #Primes start at 2
    
    # While there's still more to factor!
    while a != 1:
        
        # If the prime divides a
        if a%p == 0:
            
            # Add an entry to the factors list
            factors[p] = 0
            
            # Increment the factors count while p divides a
            while(a%p == 0):
                a //= p
                factors[p] += 1
    
        # Generate next prime and repeat!
        p = next_prime(p)
        
        # We know a is prime if none of the numbers less than
        # the sqrt of a+1 divide a, so call it a day!
        if p >= math.sqrt(a)+1:
            factors[a] = 1
            return factors

    return factors

# Controller
def prime_factors(a):

    return factor(a)


    









