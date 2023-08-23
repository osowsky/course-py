"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input( 'Digite seu nome: ' )
idade = input( 'Digite sua idade: ' )

if ( not nome ) or ( not idade ):
    print( 'Desculpe, você deixou campos vazios.' )
    exit()

print( f'Meu nome é {nome}.' )
print( f'Meu nome invertido é: {nome[::-1]}.' )
if ( ' ' in nome ):
    print( 'Menu nome contém espaços.' )
else:
    print( 'Menu nome não contém espaços.' )

# print( 'Meu nome tem %d letras.' % ( len( nome ) ) )
# print( 'Primeira e Última letras: \'%s\' e \'%s\'.' % ( nome[0], nome[-1] ) )

print( f'Meu nome tem {len( nome )} letras.' )
print( f'Primeira e Última letras: \'{nome[0]}\' e \'{nome[-1]}\'.' )
