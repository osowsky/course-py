# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# Exercício - sistema de perguntas e respostas

import os # to use the function 'system'

T_QUESTION = 'Pergunta'
T_ANSWER   = 'Resposta'
T_OPTIONS  = 'Opções'

perguntas = [
    {
        T_QUESTION: 'Quanto é 2+2?',
        T_OPTIONS: ['0', '1', '3', '4', '5'],
        T_ANSWER: '4',
    },
    {
        T_QUESTION: 'Quanto é 5*5?',
        T_OPTIONS: ['25', '55', '51'],
        T_ANSWER: '25',
    },
    {
        T_QUESTION: 'Quanto é 10/2?',
        T_OPTIONS: ['4', '5', '2', '1'],
        T_ANSWER: '5',
    },
]

 # create a sequence of letter from 'a' to the number of options.
def create_alpha_options( opt_list ):
    opt_len = len( opt_list )
    opt_res = []
    for i_letter in list( range( ord( 'a' ), ord( 'a' ) + opt_len ) ):
        opt_res.append( chr( i_letter ) )

    return opt_res


os.system( 'cls' ) #clear screen.

q_len = len( perguntas )
for q in range( 0, q_len ): # process all the test.
    question = perguntas[ q ] # get a question.

    # print the question.
    print( f'Q{q+1}: ', question.get( T_QUESTION ) )

    # print the options.
    # opt = question[ T_OPTIONS ]
    opt = question[ T_OPTIONS ]

    opt_l = create_alpha_options( opt )
    for i, o in enumerate( opt ):
        print( f'      ({opt_l[i]}) {o}' )

    # get the user answer.
    ans = ''
    while ( not ans in opt_l ):
        ans = input( f'\nType your answer ({opt_l[0]}-{opt_l[-1]}): ' )

    # check the response.
    if ( opt[ opt_l.index( ans ) ] )== question.get( T_ANSWER ):
        print( 'Your answer is right!!!' )
    else:
        print( 'Your answer is wrong!!!' )
    input( 'Press any key to continue...' )
    os.system( 'cls' )
