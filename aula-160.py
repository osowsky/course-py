# copy, sorted, produtos.sort

# use some modules.
import copy as cp
import os

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Exercício 01.
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
os.system( 'cls' )

def increase_price( lst ):
    # List comprehention.
    up_lst = [ # { **item, 'preco': item[ 'preco' ] * 1.10 } # I can use ** then overwrite the 'preco'
        { 'nome': item[ 'nome' ], 'preco': round( item[ 'preco' ] * 1.10, 2 ) } # or I can use this.
    for item in lst
    ]
    return up_lst

novos_produtos = increase_price( cp.deepcopy( produtos ) )
print( *novos_produtos, sep='\n' )
print()


# Exercício 02.
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
def sort_by_name( key ):
    return key[ 'nome' ]

# produtos_ordenados_por_nome = sorted( cp.deepcopy( produtos ),
#                                      key=sort_by_name, reverse=True )
produtos_ordenados_por_preco = sorted( cp.deepcopy( produtos ),
                                     key=lambda k: k[ 'nome' ], reverse=True )
print( *produtos_ordenados_por_preco, sep='\n' )
print()


# Exercício 03.
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
def sort_by_price( key ):
    return key[ 'preco' ]

# produtos_ordenados_por_preco = sorted( cp.deepcopy( produtos ), key=sort_by_price )
produtos_ordenados_por_preco = sorted( cp.deepcopy( produtos ),
                                     key=lambda k: k[ 'preco' ] )
print( *produtos_ordenados_por_preco, sep='\n' )
print()

