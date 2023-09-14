# Inheritance ( immaterial possession received from) (Herança não material)
#
# Class inheritance.
#

import os
from inherite import LogFileMixin, LogShellMixin
from inherite import log

ls = LogShellMixin()
ls.log_error( 'Que merda. Deu ruim.' )
ls.log_success( 'Que legal. Funcionou.' )
print()

lf = LogFileMixin( os.path.splitext( __file__ )[ 0 ] + '.log' )
lf.log_error( 'Que merda. Deu ruim.' )
lf.log_success( 'Que legal. Funcionou.' )

ls = log.LogShellMixin()
ls.log_error( 'Que merda. Deu ruim.' )
ls.log_success( 'Que legal. Funcionou.' )
print()

lf = log.LogFileMixin( os.path.splitext( __file__ )[ 0 ] + '.log' )
lf.log_error( 'Que merda. Deu ruim.' )
lf.log_success( 'Que legal. Funcionou.' )
