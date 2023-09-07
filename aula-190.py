"""
How to use generators and generator functions.
Prime number generator.

Furthermore, here it is showed the concept of visible and invisible
functions from modules that has been imported to other module.
It is used '__init__.py' and 'from .modules import *' to reach this
goal.

A generator can be created as follows:
gen = ( n for n in range( 10 ) )

Furthermore, it is used the json package to load and save a list
of prime numbers.
"""

import primef

for i in primef.count():
    print( f'prime number is { i }' )
    input( 'press any key...' )

