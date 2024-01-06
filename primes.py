from datetime import datetime

import primes_cython
import primes_pure_python


def primes_python(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes: 
        # Check if n is prime
        for i in p:
            if n % i == 0:
                break

        # If no break occurred in the loop
        else:
            p.append(n)
        n += 1
    return p

MAX = 2_500

print("Python version")
start_time = datetime.now()
primes_python(MAX)
end_time = datetime.now()
print('Duration in Python: {}'.format(end_time - start_time))

print("Pure Python version")
start_time = datetime.now()
primes_pure_python.primes_pure_python(MAX)
end_time = datetime.now()
print('Duration in Pure Python: {}'.format(end_time - start_time))

print("Cython version")
start_time = datetime.now()
primes_cython.primes_cython(MAX)
end_time = datetime.now()
print('Duration in Cython: {}'.format(end_time - start_time))
