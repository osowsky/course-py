# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

"""
There are 2 list:
to_do = []
to_redo = []

1) if a chore is created, it goes into to_do.
2) if a chore is deleted, it goes out the to_do and goes into to_redo.
3) if a chore is redone, it goes out the to_reado and goes into to_do.
4) every time that a new chore is created, the to_redo list must be
    cleaned.
"""

# Packages
import sys, os

# Lists.
to_do = []
to_redo = []

# Print options:
def print_options():
    os.system( 'cls' )
    print( 'Type a new chore or one command as below:' )
    print( '[l]ist, [u]ndo, [r]edo or [e]xit:', end=' ' ) 

# Get the option typed.
def get_option():
    # It returns:
    #  'l' -> list cmd.
    #  'u' -> undo cmd.
    #  'r' -> redo cmd.
    #  'e' -> exit cmd.
    #   '' -> error.
    #   a new chore as string.
    val_cmds = 'lure'
    opt = input( '' ).lower()

    # Check option.
    if ( opt == '' ) or ( opt in val_cmds ):
        return opt
    return opt

# List all chores on screen.
def list_chores():
    if ( len( to_do ) == 0):
        print( f'\nNo items in the list.' )
    else:
        print( f'\nChore List:' )
        for i, item in enumerate( to_do ):
            print( f'  ({i + 1}) -> {item}' )

    _ = input( f'\npress any key to continue...' )

# Remove the last item from the list.
def undo_list():
    if ( len( to_do ) == 0):
        print( f'\nNo items in the list.' )
    else:
        rem_item = to_do.pop()     # remove item from to_do.
        to_redo.append( rem_item ) # add item to to_redo.

        print( f'\nThe chore \'{rem_item}\' was removed from the list.' )
    _ = input( f'\npress any key to continue...' )

# Add the removed item to the list.
def redo_list():
    if ( len( to_redo ) == 0):
        print( f'\nNo items to redo the list.' )
    else:
        rem_item = to_redo.pop() # remove item from to_redo.
        to_do.append( rem_item ) # add item to to_do.

        print( f'\nThe chore \'{rem_item}\' was redone to the list.' )
    _ = input( f'\npress any key to continue...' )

# Main
typed_opt = ''
while ( typed_opt != 'e' ):
    print_options()
    typed_opt = get_option()
    if ( typed_opt== '' ): # nothing was typed.
        os.system( 'cls' )
        continue

    if ( typed_opt== 'e' ): # command exit.
        os.system( 'cls' )
        sys.exit( 0 )

    if ( typed_opt== 'l' ): # command list.
        list_chores()
        os.system( 'cls' )
        continue

    if ( typed_opt== 'u' ): # command undo.
        undo_list()
        os.system( 'cls' )
        continue

    if ( typed_opt== 'r' ): # command redo.
        redo_list()
        os.system( 'cls' )
        continue

    # Add a new item to the list.
    to_do.append( typed_opt )
    to_redo.clear() # list to_redo was cleaned.

    print( f'\nThe new chore \'{typed_opt}\' was added to the list.' )
    _ = input( f'\npress any key to continue...' )
