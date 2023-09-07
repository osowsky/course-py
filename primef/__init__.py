"""
A module that has a generator function that returns only prime numbers.
Likewise that the count function returns consecutive integer numbers,
this count function returns only consecutive prime numbers.
Its name is 'count' and must be imported as below:

import prime

And it must be used as follows:

p_nbr = prime.count()

for i in p_nbr:
    print( f'prime number: ' i )

REMARK: Unlike the older prime package, this primef package saves
a list of prime numbers in a JSON file at the primef directory.
This file was called 'primef.json'.
"""

# If it is used 'import prime' all elements will be exported,
# regardless of whether it is used the variable __all__.
# Note that prime.* must be used before the element.

# If it is used 'from prime import *' only elements that does not
# start with '_' will be exported.
# However, if you define the variable '__all__ = []',
# nether the elements without '_' will be exported. 
# Thus, you can put in '__all__' only that elements that you can
# export that does not begin with '_'.

# If it is used 'from prime import element, _element' that elements
# will be exported, regardless of whether it is used the variable
# __all__ 

# The outcome comes from the creation of a new file called 'count.py'
# that import everything in the package to here without '_' prefixed,
# i.e., inner variables and functions starting with '-'.
# Here, it is used the following command for importing only the
# function 'count()'
from .count import *
