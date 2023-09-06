"""
How to use generators and generator functions.
Prime number generator.

Furthermore, here it is showed the concept of visible and invisible
functions froma modules that has been imported to other module.
It is used '__init__.py' and 'from .modules import *' to reach this
goal.

A generator can be created as follows:
gen = ( n for n in range( 10 ) )
"""

# import prime
# print( next( prime.a ) )
# print( next( prime._a ) )
# prime.test()
# prime._test()


# from prime import *
# print( next( a ) )
# print( next( _a ) ) # not defined.
# _test() # not defined.
# test()


# from prime import test, _test
# print( next( a ) ) # not defined.
# print( next( _a ) ) # not defined.
# test()
# _test()

import prime

for i in prime.count():
    print( f'prime number is {i}' )
    input( 'press any key...' )

