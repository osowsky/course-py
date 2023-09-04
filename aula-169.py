# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Solution is given by using decorators, decorated functions,
# and syntax sugar.

#def param_decorador():
def decorador( func ): # decorator
    def inner_func( l_city, l_state ): #decorated function
        gap = len( l_city ) - len( l_state )
        if ( gap > 0 ):
            return func( l_city[ 0: len( l_city ) - gap ], l_state )
        elif ( gap < 0 ):
            return func( l_city, l_state[ 0: len( l_state ) + gap ] )
        else:
            return func( l_city, l_state )
            
    return inner_func
#    return decorador

# @param_decorador() # syntax sugar.
@decorador # syntax sugar.
def list_union( l_city, l_state ):
    return [ ( l_city[ i ], l_state[ i ] )
        for i in range( len( l_city ) )
    ]


cities = [ 'Salvador', 'Ubatuba', 'Belo Horizonte' ]
states = [ 'BA', 'SP', 'MG', 'RJ' ]

print( *list_union( cities, states ), sep='\n' )
