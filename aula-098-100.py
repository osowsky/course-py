"""
AULA 098:
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Type an CPF and check if it has the correct size.
szCPF = input( ' Type a CPF ( only eleven numbers): ' )
# szCPF = '74682489070' # A CPF for testing.
CPFLen = len( szCPF )
if ( CPFLen != 11 ):
    print( 'An CPF MUST have eleven numbers. You type an invalid CPF.' )
    exit( 0 )

# CPF only has to have number.
if ( not szCPF.isdecimal() ):
    print( 'An CPF MUST have eleven numbers. You type an invalid CPF.' )
    exit( 0 )

# CPF can not have eleven equal numbers.
if ( szCPF[0] * len( szCPF ) == szCPF ):
    print( 'An CPF can\'t have eleven equal numbers. You type an invalid CPF.' )
    exit( 0 )

# Create an enumerated tuple from the CPF, by using reversed function
# or decreased index range.
tpCPF = tuple( enumerate( reversed( szCPF ) ) )
# or 
# tpCPF = tuple( enumerate( szCPF[ ::-1 ] ) )

# Find the tens of CPF's checking digit.
iSum = 0
for idx, nbr in tpCPF:
    if ( idx < 2 ):
        continue
    iSum += idx * int( nbr )

"""
# Check if the tens of CPF's checking digit is ok.
if ( ( iSum * 10 ) % 11 ) != int( tpCPF[ 1 ][ 1 ] ):
    print( 'Your CPF\'s number is invalid. Please contact the PF.' )
    exit( 0 )
"""
# Use ternary operator to get the CPF's checker.
r = ( iSum * 10 ) % 11
iChecker = 0 if ( r > 9 ) else ( r * 10 )

"""
AULA 100:
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
# Create an enumerated tuple from the CPF, by using reversed function
# starting from 1.
tpCPF = tuple( enumerate( reversed( szCPF ), 1 ) )

# Find the tens of CPF's checking digit.
iSum = 0
for idx, nbr in tpCPF:
    if ( idx < 2 ):
        continue
    iSum += idx * int( nbr )

# Use ternary operator to get the other CPF's checker.
r = ( iSum * 10 ) % 11
iChecker += 0 if ( r > 9 ) else r

# Check the CPF.
if ( iChecker == int( szCPF[ -2::1 ] ) ):
    print( 'Your CPF is valid!' )
else:
    print( 'Your CPF is invalid!' )
