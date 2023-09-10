# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class DoAnyThing:
    def __init__( self, a = 0, b = 0 ):
        self._a = a
        self._b = b

    @classmethod
    def Create( cls, a, b, / ):
        return cls( a, b )

    @staticmethod
    def Init( a = 0, b = 0  ):
        return DoAnyThing( a, b )

    def print( self ):
        print( f'{ self.a= } and { self.b= }' )

    @property
    def a( self ):
        return self._a

    @property
    def b( self ):
        return self._b

    @a.setter
    def a( self, a ):
        self._a = a

    @b.setter
    def b( self, b ):
        self._b = b

################################################
a1 = DoAnyThing()
a2 = DoAnyThing.Create( 10, 20 )
a3 = DoAnyThing.Init()
a4 = DoAnyThing.Init( 15, 30 )


a1.print()
a2.print()
a3.print()
a4.print()

a1.a = 1
a1.b = 2
print( a1.a, a1.b )
