"""
CPF generator.
"""
import random as rnd

# Create a random CPF. only the first 9 digits.
CPF_LEN = 11 # number of digits for a valid CPF.
szCPF = ''
for _ in range( 0, CPF_LEN - 2 ):
    szCPF += str( rnd.randint( 0, 9 ) )

# Create an enumerated tuple from the CPF, by using reversed function
# or decreased index range.
tpCPF = tuple( enumerate( reversed( szCPF ), 2 ) )
# or 
# tpCPF = tuple( enumerate( szCPF[ ::-1 ] ) )

# Find the tens of CPF's checking digit.
iSum = 0
for idx, nbr in tpCPF:
    iSum += idx * int( nbr )

# Use ternary operator to get the CPF's checker.
r = ( iSum * 10 ) % 11
iChecker = 0 if ( r > 9 ) else r

# Add the checker to the CPF.
szCPF = szCPF + str( iChecker )

# starting from 1.
tpCPF = tuple( enumerate( reversed( szCPF ), 2 ) )

# Find the units of CPF's checking digit.
iSum = 0
for idx, nbr in tpCPF:
    iSum += idx * int( nbr )

# Use ternary operator to get the other CPF's checker.
r = ( iSum * 10 ) % 11
iChecker = 0 if ( r > 9 ) else r

# Add the checker to the CPF.
szCPF = szCPF + str( iChecker )
print( f'Your valid CPF is: {szCPF}' )
