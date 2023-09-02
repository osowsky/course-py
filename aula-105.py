# How a function treats its arguments.
# Immutable args are passed to the function by value.
# Mutable args are passed to the function by reference.

def test( n, f, sz, t, l, d, s ):
    n = 10
    f = 4.55
    sz = 'xyz'
    l[ 0 ] = 10
    d['a'] = 2
    s.add( 4 )
    

n = 1           # int
f = 2.45        # float
sz = 'abc'      # string
t = ( 1, 2 )    # tuple
l = [ 1, 2, 3 ] # list
d = { 'a': 1 }  # dict
s = { 1, 2, 3 } # set

print( n, f, sz, t, l, d, s )
test( n, f, sz, t, l, d, s )
print( n, f, sz, t, l, d, s )

