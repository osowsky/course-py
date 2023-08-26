"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

KEY_WORD = 'jefferson e josiane' # work to be found (key work).
KEY_WORD_LEN = len( KEY_WORD ) # its length.

test_word = KEY_WORD_LEN * '*' # work to be tested.
attempts = 0 # number of attempts.

# Play the game.
while ( test_word != KEY_WORD ):
    print( 'Word:', test_word, '\t', 'Attempts:', attempts )
    letter = input( 'Type a letter (a-z or space): ' )
    
    if ( len( letter ) != 1 ): # test the letter size.
        attempts += 1
        continue
    
    if ( not ( letter in KEY_WORD ) ): # the letter is in the key work.
        attempts += 1
        continue

    # show this letter in the tested word.
    word = ''
    for l in range( KEY_WORD_LEN ):
        if ( KEY_WORD[ l ] == letter ):
            word = word + letter
        elif ( test_word[ l ] == '*' ):
            word = word + '*'
        else:
            word = word + KEY_WORD[ l ]
    test_word = word
    attempts += 1

print( f'Congrats: You have found the key word \'{KEY_WORD}\'.' )
print( f'The have reached it in {attempts} attempts.' )


