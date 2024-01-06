import cython


def primes_pure_python(nb_primes: cython.int):
    i: cython.int
    p: cython.int[2500]

    if nb_primes > 2500:
        nb_primes = 2500

    if not cython.compiled:  # Only if regular Python is running
        p = [0] * 2500       # Make p work almost like a C array

    # The current number of elements in p
    len_p: cython.int = 0  
    n: cython.int = 2

    while len_p < nb_primes:
        # Check if n is prime
        for i in p[:len_p]:
            if n % i == 0:
                break
        else:
            # add prime number to the list
            p[len_p] = n
            len_p += 1
        n += 1

    # Copy the result into a Python list:
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list

