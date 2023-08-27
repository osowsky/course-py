"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

shopping = [] # shopping list.
option = ''   # typed option.
product = ''

while ( option != 'e' ):
    # Choose an option.
    os.system( 'cls' )
    option = input( 'Options: [a]dd, [d]elete, [l]ist, [e]xit: ' ).lower()
    
    if ( len( option ) != 1): # option must be only one letter.
        continue

    # Action to be done.
    if ( option == 'a'):    # adding an item to the shopping list.
        product = input( 'Add a product to your shopping list: ' ).lower()
        if ( not product ):
            print( 'No products have been added to your shopping list.' )
        else:
            if ( product in shopping ):
                print( 'This product is already in your shopping list.' )
            else:
                shopping.append( product )
                print( f'One {product} has been added to your shopping list.' )
    elif ( option == 'd' ): # deleting an item in the shopping list.
        print( 'shopping list:' )
        print( '\tItem \tProduct' )
        for idx, item in enumerate( shopping ):
            print( f'\t {idx + 1} \t {item}' )
        str_item = input( 'Type the item you want to delete from your shopping list: ' )
        try: # I don't like to use it.
            num_item = int( str_item ) - 1
            if ( num_item < 0 ):
                print( 'Couldn\'t delete this item from your shopping list.' )
            else:
                product = shopping.pop( num_item )
                print( f'The {product} has been deleted from your shopping list.' )
        except:
            print( 'Couldn\'t delete this item from your shopping list.' ) 
    elif ( option == 'l' ): # listing the shopping list.
        print( 'shopping list:' )
        print( '\tItem \tProduct' )
        for idx, item in enumerate( shopping ):
            print( f'\t {idx + 1} \t {item}' )
    else:
        continue

    print( 'Press any key to continue...' )
    input()

print( 'Thanks for using our services. Good bye!' ) # final message.
