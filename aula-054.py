"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
# We can also use:
try:
    ... # try to do something.
except:
    ... # raise an exception if try fails.

# but, I preferred to use the following code.
"""

"""
number = input( 'Type an integer number: ' )

if ( not len( number ) ): # was something typed?
    print( 'Error: you didn\'t type any character!' )
    exit( 0 )

number = number.lstrip() # remove leading whitespaces.
if ( number[0] == '-' ): # remove negative sign if it exists.
    number = number.replace( '-', '', 1 )
if ( not number.isdecimal() ): # check if it is ok. use decimal instead of digit.
    print( 'Error: you didn\'t type an integer number!' )
    exit( 0 )

remainder = int( number ) % 2 # get the remainder of the division by 2.
if (  remainder ):
    print( f'The number {number} is odd.' )
else:
    print( f'The number {number} is even.' )
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
hour = input( 'Type an hour (0-23): ' )

if ( not len( hour ) ): # was something typed?
    print( 'Error: you didn\'t type any character!' )
    exit( 0 )

if ( not hour.isdecimal() ): # check if it is ok. use decimal instead of digit.
    print( 'Error: you should have typed an integer number between 0 and 23!' )
    exit( 0 )

ihour = int( hour )
if ( ihour >= 0 ) and ( ihour <= 11 ):
    print( 'Good morning!' )
elif ( ihour >= 12 ) and ( ihour <= 17 ):
    print( 'Good afternoon!' )
elif ( ihour >= 18 ) and ( ihour <= 23 ):
    print( 'Good evening!' )
else:
    print( 'Error: you should have typed an integer number between 0 and 23!' )
    exit( 0 )
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
name = input( 'Type your name: ' )

if ( not len( name ) ): # was something typed?
    print( 'Error: you didn\'t type any character!' )
    exit( 0 )

name = name.lstrip() # remove leading whitespaces.
name_len = len( name )

if ( name_len <= 4 ):
    print( 'You name is short!' )
elif ( name_len >= 5  ) and ( name_len <= 6  ):
    print( 'You name is common!' )
else:
    print( 'You name is very long!' )
"""
