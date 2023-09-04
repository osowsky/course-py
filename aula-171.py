"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

l_a = [ 10, 20, 30, 40, 50, 60, 70 ]
l_b = [ 1, 2, 3, 4 ]

"""
My solution.
rng = min( len( l_a ), len( l_b ) )
l_a_b = [ l_a[ i ] + l_b[ i ]
    for i in range( rng )
]
"""

"""
Best solution.
"""
l_a_b = [ x + y
    for x, y in zip( l_a, l_b )
]

print(l_a, '+', l_b, '=', l_a_b, sep='\n' )
