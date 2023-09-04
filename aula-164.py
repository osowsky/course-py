# free variables and nonlocal variables.

def concate( val_ini ):
    val_end = val_ini

    def concate_with( val ):
        nonlocal val_end # use to access val_end in concate.

        val_end = val_end + val
        return val_end
    
    return concate_with

c = concate( 'a' )
print( c( 'b' ) )
