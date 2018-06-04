#Program for prime factorization, output {prime,count/power...}
import math

def _prime_factors(a):

    primes = []
    factors = {}

    num = a

    #Populate list of primes with all possible primes in factorization
    for i in range (2,int(num/2)+1):
        primes.append(i)
        for j in range(2,int(math.sqrt(i))+1):
            if i%j == 0:
                primes.remove(i)
                break

    #Determine prime facotrization
    for p in primes:

        if num == 0:
            break

        if num%p == 0:

            factors[p]=0

            while(num%p == 0):
                num = num/p
                factors[p] += 1

    return factors


def prime_factors(n):

	p = _prime_factors(n); print("p",p)


	if len(p) == 0:
		return n
	else:
		return p
