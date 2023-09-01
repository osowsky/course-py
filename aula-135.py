"""
Pack and unpack arguments (*args) and keyword arguments (**kwargs).
"""

def print_packed_args( *args, **kwargs ):
    print( 'first: ', args, type( args ) )
    print( 'second: ', kwargs, type( kwargs ) )

def print_unpacked_args( *args, **kwargs ):
    print( 'first: ', *args )
    print( 'second: ', *kwargs )
    print( 'third: ', kwargs.items(), type( kwargs.items() ) )
    print( 'fourth: ', kwargs.keys(), type( kwargs.keys() ) )
    print( 'fifth: ', kwargs.values(), type( kwargs.values() ) )


print_packed_args( 1, 2, 3, 4, name='jeff', sname='osowsky', age=51 )
print()
print_unpacked_args( 1, 2, 3, 4, name='jeff', sname='osowsky', age=51 )
