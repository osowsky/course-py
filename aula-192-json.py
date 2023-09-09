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
import json

# Lists.
to_do = []
to_redo = []
file_name = ''

# Constants
DICT_KEY = 'chore_'

# Get json file name.
def get_json_file():
    # create the path+name of the .json file.
    return os.path.splitext( __file__ )[ 0 ] + '.json'

def load_list():
    global file_name

    d = dict() # create a empty dictionary.

    # create a json file.
    file_name = get_json_file()

    # check if the file exist.
    if ( not os.path.isfile( file_name ) ):
        return
    
    # read a json file.
    with open( file_name, 'r', encoding = 'utf-8' ) as f_json:
        d = json.load( f_json )

    # Fill out the list with the dictionary.
    for key, val in d.items():
        to_do.append( val )

def save_list():
    global file_name

    if ( len( to_do ) == 0 ): # list is empty.
        print( f'\nERROR: The chore list is empty. Nothing to save.' )
        _ = input( f'\npress any key to continue...' )
        return

    d = dict() # create a empty dictionary.
    
    # create a json file.
    file_name = get_json_file()

    # Fill out the dictionary with the list.
    for i, item in enumerate( to_do ):
        d[ f'{DICT_KEY}{i}' ] = item

    # create json file.
    with open( file_name, 'w', encoding = 'utf-8' ) as f_json:
        json.dump( d, f_json, ensure_ascii = False, indent = 2 )

    print( f'\nThe chore list was saved as {file_name}' )
    _ = input( f'\npress any key to continue...' )

# Print options:
def print_options():
    os.system( 'cls' )
    print( 'Type a command to handle your chore list:' )
    print( '[a]dd, [l]ist, [u]ndo, [r]edo, [s]ave or [e]xit:',
           end=' ' ) 

# Get the option typed.
def get_option():
    # It returns:
    #  'a' -> add cmd.
    #  'l' -> list cmd.
    #  'u' -> undo cmd.
    #  'r' -> redo cmd.
    #  's' -> save cmd.
    #  'e' -> exit cmd.
    #   '' -> error.
    #   a new chore as string.
    val_cmds = 'alurse'
    opt = input( '' ).lower()

    # Check option.
    if ( opt == '' ) or ( opt in val_cmds ):
        return opt
    return opt

# Add a new chore to the list.
def add_chore():
    new_chore = input( f'  Type a new chore: ' )
    if ( new_chore == '' ):
        print( f'\nERROR: No chore was typed. Try again.' )
    else:
        to_do.append( new_chore )
        to_redo.clear() # list to_redo was cleaned.
        print( f'\nThe new chore \'{new_chore}\' was added to the list.' )

    _ = input( f'\npress any key to continue...' )

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


# Another approach for solving this problem.
# Instead of using the command 'if-else' to choose the right command.
# It is created a dictionary that call all functions for each option.
# Dictionary of options and functions:
commands = {
    'a': lambda: add_chore(),
    'l': lambda: list_chores(),
    'u': lambda: undo_list(),
    'r': lambda: redo_list(),
    's': lambda: save_list(),
    'e': lambda: sys.exit( 0 )
     }

# Main
typed_opt = ''

load_list() # Load a chore list from a json file.

while ( typed_opt != 'e' ):
    print_options()
    typed_opt = get_option()
    if ( typed_opt == '' ):
        continue
 
    # Execute the desired command.
    cmd = commands[ typed_opt ]
    if ( typed_opt == 'e' ):
        os.system( 'cls' )
    cmd()
