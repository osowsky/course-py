"""
Class LogMixin
Class LogShellMixin
Class LogFileMixin
"""

import sys, os
# from pathlib import Path

"""
Functions and variables that are visible to other modules.
"""
__all__ = [ 'LogShellMixin', 'LogFileMixin' ]


"""
Class LogMixin (An abstract class).
"""
class LogMixin:
    def _log( self, msg ):
        msg =  'Abstract method. Please, implement it in a child class.'
        raise NotImplementedError( f'From { self.__class__.__name__ }: { msg }' )
    
    def log_error( self, msg ):
        return self._log( f'Error From { self.__class__.__name__ }: { msg }' )

    def log_success( self, msg ):
        return self._log( f'Success From { self.__class__.__name__ }: { msg }' )


"""
Class LogShellMixin (print messages in stdout and/or stderr).
"""
class LogShellMixin( LogMixin ):
    def _log( self, msg ):
        if ( 'Error From' in msg ):
            print( f'{ msg }', file = sys.stderr )
        elif ( 'Success From' in msg ):
            print( f'{ msg }', file = sys.stdout )
        else:
            print( f'{ msg }' )


"""
Class LogFileMixin (print messages in a file).
"""
class LogFileMixin( LogMixin ):
    def __init__( self, filename = os.path.splitext(__file__)[ 0 ] + '.txt' ):
        self._filename = filename

    def _log( self, msg ):
        with open( self._filename, 'a' ) as flog:
            print( msg, file = flog )


"""
Debug area.
Used when log.py is executed.
"""
if __name__ == '__main__':
    try:
        l = LogMixin()
        l._log( 'hello, world!!!' )
    except NotImplementedError as e:
        print( f'{e.__class__.__name__}:', *e.args, '\n' )

    try:
        l = LogMixin()
        l.log_error( 'calling log_error method.' )
    except NotImplementedError as e:
        print( f'{e.__class__.__name__}:', *e.args, '\n' )

    ls = LogShellMixin()
    ls.log_error( 'Que merda. Deu ruim.' )
    ls.log_success( 'Que legal. Funcionou.' )
    print()

    lf = LogFileMixin()
    lf.log_error( 'Que merda. Deu ruim.' )
    lf.log_success( 'Que legal. Funcionou.' )
    print()
