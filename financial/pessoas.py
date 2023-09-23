from os import path

__all__ = [ 'Pessoa', 'Cliente' ]

__file = path.basename( path.splitext( __file__ )[0] )
__file_names = [ '__main__', __file ]
if ( __name__ in __file_names ):
    import contas
else:
    from . import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)
