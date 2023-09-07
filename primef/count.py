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
import os
import json

"""
Internal variables.
"""
_prime_lst = [ 2, 3 ]
_file_name = ''

"""
Internal functions.
"""
def _is_prime( num ):
    for prime in _prime_lst:
        if ( num % prime == 0 ):
            return False
    
    # 'num' is prime.
    return True 

def _count_decor( func ): # decorator
    global _prime_lst
    global _file_name

    # create the path+name of the .json file.
    cur_dir = os.path.dirname( __file__ )
    _file_name = cur_dir + '/' + os.path.basename( cur_dir ) + '.json'
    
    # check if the file exist.
    if ( os.path.isfile( _file_name) ):
        # read json file.
        with open( _file_name, 'r', encoding = 'utf-8' ) as f_json:
            _prime_lst = json.load( f_json )[ 'primes' ]
    else:
        # create json file.
        with open( _file_name, 'w', encoding = 'utf-8' ) as f_json:
            json.dump( dict( primes = _prime_lst ), f_json,
                       ensure_ascii = False, indent = 2 )

    def inner_func(): #decorated function
        # call function count().
        # As count is a generator function, after it is called
        # the inner_func will not be run again.
        return func()
    
    return inner_func

"""
External variables.
"""
...

"""
External functions.
"""
@_count_decor #call the decorator of the count function.
def count():
    """
     A prime number generator. This integer counter returns the next prime
     number starting from 2. Furthermore, a list of prime numbers is saved
     in the file 'primef.json'.
    """
    global _prime_lst
    global _file_name
    
    # return the primes in the list.
    for prime in _prime_lst:
        yield prime

    # return the others primes.
    odd_counter = it.count( start = _prime_lst[ -1 ] + 2,
                            step = 2 ) # odd number counter.
    while ( True ):
        odd_num = next( odd_counter )
        if ( _is_prime( odd_num ) ):
            _prime_lst.append( odd_num ) # Add this number to the list.
            
            # rewrite json file.
            with open( _file_name, 'w', encoding = 'utf-8' ) as f_json:
                json.dump( dict( primes = _prime_lst ), f_json,
                           ensure_ascii = False, indent = 2 )
        
            yield odd_num
