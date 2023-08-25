"""
Bu using command 'while' for handling strings.
"""
name = 'Hello, world!'
handled = ''

ilen  = len( name )
i = 0
while ( i < ilen ):
    print( name[ i ], end='' )
    handled += '*' + name[ i ]
    i += 1
handled += '*'

print( '' )
print( handled )
