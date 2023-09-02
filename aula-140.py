# List comprehension.

import os

os.system( 'cls' ) # clear screen.

# General.
lc_01 = [ n for n in range( 0, 10 ) ]
print( lc_01, '\n' )

# With mapping.
lc_02 = [ 2 * n
          for n in range( 0, 10 ) ]
print( lc_02, '\n' )

# With mapping and conditional.
lc_03 = [ 2 * n if ( n % 2 ) == 0 else n
          for n in range( 0, 10 ) ]
print( lc_03, '\n' )

# With mapping and conditional and filter.
# Filter has precedence between the mapping.
# See lc_05.
lc_04 = [ 2 * n if ( n % 2 ) == 0 else n
          for n in range( 0, 10 )
           if ( n % 2 ) == 0 ]
print( lc_04, '\n' )

# Filter.
lc_05 = [ 2 * n
          for n in range( 0, 10 )
           if ( n % 2 ) == 0 ]
print( lc_05, '\n' )
