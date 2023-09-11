# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

"""
associação, agregação e composição.

Pilares da OOP:
    Abstração.
    Encapsulamento.
    Polimorfismo.
    Herança.
"""

# Car class.
class Car:
    def __init__( self, name = None ) -> None:
        self._name = name
        self._engine = Engine()
        self._factory = Factory()

    @property
    def name( self ) -> str:
        return str( self._name )
    
    @property
    def engine( self ):
        return self._engine
    
    @property
    def factory( self ):
        return self._factory
    
    @name.setter
    def name( self, name ) -> None:
        self._name = name

    @engine.setter
    def engine( self, engine ) -> None:
        self._engine = engine
    
    @factory.setter
    def factory( self, factory ) -> None:
        self._factory = factory

    def print_props( self ) -> None:
        print( f'Car name: { self.name } -- ', end = '' )
        print( f'Engine: { self.engine.name } -- ', end = '' )
        print( f'Manufacturer: { self.factory.name }' )
    
    def __del__( self ) -> None:
        print( f'deleting { self.__class__.__name__ } with { self.name=}' )

#--------------------------------------------------------------------
# Engine class.
class Engine:
    def __init__( self, name = None ) -> None:
        self._name = name

    @property
    def name( self ) -> str:
        return str( self._name )

    @name.setter
    def name ( self, name ) -> None:
        self._name = name

    def __del__( self ) -> None:
        print( f'deleting { self.__class__.__name__ } with { self.name=}' )

#--------------------------------------------------------------------
# Factory class.
class Factory:
    def __init__( self, name = None ) -> None:
        self._name = name
        self._cars = []

    def insert_car( self, name, engine ) -> None:
        new_car = Car( name )
        new_car.engine.name = engine
        new_car.factory.name = self.name
        self._cars.append( new_car )

    def print_cars( self ) -> None:
        for car in self._cars:
            car.print_props()

    @property
    def name( self ) -> str:
        return str( self._name )

    @name.setter
    def name ( self, name ) -> None:
        self._name = name

    def __del__( self ) -> None:
        print( f'deleting { self.__class__.__name__ } with { self.name=}' )

#--------------------------------------------------------------------
# Main
c1 = Car( 'Uno' )
c2 = Car( 'Gol' )
c3 = Car( 'Chevette' )

c1.engine.name = 'V4 1.0'
c2.engine.name = 'V6 1.4'
c3.engine.name = 'V8 2.0'

c1.factory.name = 'Fiat'
c2.factory.name = 'Volkswagen'
c3.factory.name = 'Chevrolet'

print()
c1.print_props()
c2.print_props()
c3.print_props()
print()

f = Factory( 'Fiat' )
f.insert_car( 'Uno', 'V4 1.0' )
f.insert_car( 'Oggi', 'V4 1.0' )
f.insert_car( 'Punto', 'V6 1.6' )
f.print_cars()

print()
