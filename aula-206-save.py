# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
import varname as vn # pip install --upgrade varname

class Family():
    def __init__( self, father = None, mother = None ):
        self.father = father
        self.mother = mother
        self.children = []
        self.instance_name = vn.varname()

    def save( self ):
        # Get the file name that is equal to the instance name.
        file_name = ( str( self.instance_name ) + '.json' )
        # Save this instance as json.
        with open( file_name, 'w', encoding = 'utf-8' ) as f_json:
            json.dump( vars( self ), f_json, ensure_ascii = False, indent = 2 )


    def add_child( self, child ):
        self.children.append( child )

    def print( self ):
        print( f'The father is {self.father}' )
        print( f'The mother is {self.mother}' )
        print( f'The kids is/are:' )
        for child in self.children:
            print( f'   {child}' )


############################################
# Main

f1 = Family( 'Jeff', 'Josi' )
f1.add_child( 'Daniel' )
f1.add_child( 'Emanuelle' )
f1.save()
f1.print()
