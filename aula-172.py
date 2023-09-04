"""
Uma outra possibilidade é usar zip_longest para capturar
os valores da lista maior.
A ideia é a mesma, veja:
"""

from itertools import zip_longest
 
l_a = [10, 20, 30, 40, 50]
l_b = [12, 2, 3, 6, 50, 60, 70]

l_a_b = [x + y for x, y in zip_longest(l_a, l_b, fillvalue=0)]
print(l_a, '+', l_b, '=', l_a_b, sep='\n' )

"""
Neste caso, usamos o "fillvalue" como 0 (zero),
assim conseguimos capturar os valores restantes da lista maior,
realizando contas, sem obter um erro em nosso programa.
"""
