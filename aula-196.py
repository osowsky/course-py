# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma_0(a, b, /, *, c, d, **kwargs):
    print( kwargs )
    print(a + b + c + d )

def soma_1(a, b, /, c, d, **kwargs):
    print( kwargs )
    print(a + b + c + d )

def soma_2(a, b, /, *args, **kwargs ): #, c, d, **kwargs):
    print( args )
    print( kwargs )
    print(a + b )

soma_0(1, 2, c=3, d=4, nome='teste' )
print()
soma_1(1, 2, 3, 4, nome='teste' )
print()
soma_2(1, 2, 3, 4, nome='teste' )