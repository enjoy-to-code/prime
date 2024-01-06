# primes_cython.pyx
# cython: boundscheck=False 
# cython: cdivision=True
# cython: initilizedcheck=False
# cython: unraisable_traceback=False
# cython: binding=False

#
# BUILD with: python setup.py build_ext --inplace
#
def primes_cython(int nb_primes):
    cdef int n, i, len_p
    cdef int[2500] p

    if nb_primes > 2500:
        nb_primes = 2500

    len_p = 0  # The current number of elements in p.

    n = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.

        else:
            p[len_p] = n
            len_p += 1
        n += 1


    # Let's copy the result into a Python list:
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list