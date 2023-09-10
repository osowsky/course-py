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

    def load( self ):
        # Get the file name that is equal to the instance name.
        file_name = ( str( self.instance_name ) + '.json' )

        # Load this instance from json.
        with open( file_name, 'r', encoding = 'utf-8' ) as f_json:
            self.__dict__ = json.load( f_json )

        # Fill out the variables.


    def print( self ):
        print( f'The father is {self.father}' )
        print( f'The mother is {self.mother}' )
        print( f'The kids is/are:' )
        for child in self.children:
            print( f'   {child}' )

############################################
# Main

f1 = Family()
f1.load()
f1.print()
