"""
Exercícios.
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.

Use HPF, FCF, Closure, and so on.
"""

def multiplication( multiplier ):
    def mult_by( operating ):
        return multiplier * operating
    
    return mult_by

multi_by_2 = multiplication( 2 )
multi_by_3 = multiplication( 3 )
multi_by_4 = multiplication( 4 )
multi_by_5 = multiplication( 5 )

value = 10.0
print( f'2 * {value} = {multi_by_2( value )}' )
print( f'3 * {value} = {multi_by_3( value )}' )
print( f'4 * {value} = {multi_by_4( value )}' )
print( f'5 * {value} = {multi_by_5( value )}' )
