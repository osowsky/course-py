# Doc Strings

"""
This a test module.

It will show to you how to use doc strings
with a module, a class and methods in a class.
"""

class A:
    """
    Class A.
    
    This class do something that I do not know.
    """

    def do_something( self ):
        """
        Method do_something.
        
        do_something is a method of the class A.
        """
        ...

"""
This a test module.

It will show to you how to use doc strings
with a module, a class and methods in a class.
"""

class B( A ):
    """
    Class B.
    
    This class is a subclass of A and do something that I do not know.
    """

    def do_something( self ):
        """
        Method do_something.
        
        do_something is a method of the class B.
        """
        ...


help( A )
print()
help( B )
print( A.__dir__ )
print()
print( dir() )
print()
print( dir( A ) )
