# How to use Emun.

import enum

direction = enum.Enum( 'directions', [ 'LEFT', 'RIGHT', 'UP', 'DOWN' ] )


print( direction.LEFT in direction ) # True
print( isinstance( direction.LEFT, direction ) ) # True
print( direction( 1 ) ) # dir.LEFT
print( direction( 1 ) == direction[ 'LEFT' ] ) # True
print( direction( 1 ) == direction.LEFT ) # True
print( direction( 1 ).value ) # 1
print( direction( 1 ).name ) # LEFT
print( direction( 1 ).value == 1 ) # True
print( direction( 1 ).name == 'LEFT' ) # True
print()

class Direction( enum.Enum ):
    LEFT = 1   # enum.auto()
    RIGHT = 2
    UP = 3
    DOWN = 4


dir = Direction
print( dir.DOWN, dir.DOWN.name, dir.DOWN.value )
