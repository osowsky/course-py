"""
A module that has three classes:

LogMixin (An abstract class)

LogMixin -> LogShellMixin

LogMixin -> LogFileMixin
"""

# If it is used 'import prime' all elements will be exported,
# regardless of whether it is used the variable __all__.
# Note that prime.* must be used before the element.

# If it is used 'from prime import *' only elements that does not
# start with '_' will be exported.
# However, if you define the variable '__all__ = []',
# nether the elements without '_' will be exported. 
# Thus, you can put in '__all__' only that elements that you can
# export that does not begin with '_'.

# If it is used 'from prime import element, _element' that elements
# will be exported, regardless of whether it is used the variable
# __all__ 

# The outcome comes from the creation of a new file called 'count.py'
# that import everything in the package to here without '_' prefixed,
# i.e., inner variables and functions starting with '-'.
# Here, it is used the following command for importing only the
# function 'count()'
from .contas import *
from .pessoas import *
from .banco import *

