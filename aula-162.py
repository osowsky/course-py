# Exercício - Adiando execução de funções

def soma( x, y ):
    return x + y


def multiplica( x, y, z ):
    return x * y * z


"""
My solution.
def soma( x ):
    def soma_x_y( y ):
        return x + y
    
    return soma_x_y


def multiplica( x ):
    def multiplica_x_y( y ):
        return x * y
    
    return multiplica_x_y


def criar_funcao( funcao, *args ):
    return funcao( *args )
"""

def criar_funcao( funcao, *args0 ):
    def wait_for( *args1 ):
        return funcao( *args0, *args1 )
    
    return wait_for

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

y = 10
z = 20
print( f'5 + { y= } = { soma_com_cinco( y )}' )
print( f'10 * { y= } * { z= } = { multiplica_por_dez( y, z ) }' )
