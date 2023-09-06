"""
Use '_' to constrain variables and functions from the external
environment.
"""

"""
Functions and variables that are visible to other modules.
"""
__all__ = [ 'count' ]

"""
Imported modules.
"""
import itertools as it

"""
Internal variables.
"""
_prime_lst = [ 2, 3 ]

"""
Internal functions.
"""
def _is_prime( num ):
    for prime in _prime_lst:
        if ( num % prime == 0 ):
            return False
    
    # 'num' is prime.
    # Add it to the list.
    _prime_lst.append( num )
    return True 

"""
External variables.
"""
...

"""
External functions.
"""
def count():
    """
     A prime number generator. This integer counter returns the next prime
     number starting from 1.
    """
    # return the primes in the list.
    for prime in _prime_lst:
        yield prime

    # return the others primes.
    odd_counter = it.count( start = _prime_lst[ -1 ] + 2, step = 2 ) # odd number counter.
    while ( True ):
        odd_num = next( odd_counter )
        if ( _is_prime( odd_num ) ):
            yield odd_num
