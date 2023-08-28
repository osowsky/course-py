# Scope and global variables.
# global variable in a internal function only assesses and modifies
# external variables declared in the scope of the current module. 

x = 1

def fn_1st_level():
    x = 2

    def fn_2nd_level():
        global x    # This 'x' refers to 'x' of the module ( x = 1 ). 
        print( 'fn_2nd_level:', x )
        x = 3
        print( 'fn_2nd_level:', x )

    print( 'fn_1st_level:', x )
    fn_2nd_level()
    print( 'fn_1st_level:', x )

print( 'module_level:', x )
fn_1st_level()
print( 'module_level:', x )
