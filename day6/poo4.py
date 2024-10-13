#!/usr/bin/env python3

# Classe que indica que uma classe é abstrata através de herança
from abc import ABC

# Herança + Abstração


# Classe que abstrai a representação de uma pessoa
class Person:
    kingdom = "animalia"


# Classe que abstrai a representação de um animal
class Animal:
    kingdom = "animalia"


# Classe pai / super classe / classe base
# Herdeiro da classe `ABC`
# Classe abstrata que representa uma fruta
class Fruit(ABC):
    kingdom = "vegetalia"

    def __init__(self, colors):
        self.colors = colors


# Classe pai / super classe / classe base
# Herdeira da classe `ABC`
# Classe abstrata que representa uma comida
class Food(ABC):
    price = 4.5


# Classe derivada ou classe material, representa de fato uma fruta,
# no caso, uma maçã através de herança
# Nesse caso, ela herda de duas classes, pois Maçã é uma fruta e uma comida
class Apple(Fruit, Food):
    pass


# Mesmo caso acima, a diferença é que essa fruta é uma Melância e
# não é uma comida
class Watermelon(Fruit):
    pass


# Acessando os atributos das classes pai através da classe herdeira
minha_maca = Apple(colors=["green", "white"])
print(minha_maca.colors)
print(minha_maca.kingdom)
print(minha_maca.price)

minha_melancia = Watermelon(["green", "red", "black"])
print(minha_melancia.colors)
print(minha_melancia.kingdom)

# Polimorfismo


# Classe que representa um cachorro e faz um som
class Dog:
    def make_sound(self):
        return "woof woof"


# Classe que representa um gato e também faz um som
class Cat:
    def make_sound(self):
        return "meow meow"


# Método que imprime o som que um objeto faz,
# no caso, qualquer objeto que tenha esse comportamento é
# aceitado nessa função
# Isso é uma função polifórmica, ou seja, aceita qualquer objeto que
# faz um som
def print_sound(obj):  # Soundable
    if not hasattr(obj, "make_sound"):
        raise ValueError(f"{obj} is not Soundable")
    print(obj.make_sound())  # implementa make_sound


# Imprimindo os sons de ambos animais
rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)

# Nesse caso, o número `42` não possui a ação de realizar um som,
# ou seja, ela não pode executar essa função
# print_sound(42)

# Duck Typing
"""
Se o objeto anda como um pato,
parece um pato, faz quack como um pato
então é um pato
"""


# Maneira de tornar uma função polimórfico, no caso,
# ela aceita n elementos ou nenhum elemento, não é fixo
def funcao(*args):
    ret = 0
    for arg in args:
        ret += arg

    return ret


# Chamadas da função polimórfica
print(funcao(1, 2, 3))
print(funcao(1, 2, 3, 4))
print(funcao())

# Encapsulamento

# Convenção de nomes


# Classe que representa uma conta bancária
class Conta:
    # Atributo protegido / protected
    _tipo_de_conta = "corrente"
    # Atributo privado / private
    __id_interno = 456789

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    # Maneira correta de acessar um valor para um atributo protegido,
    # através de um método getter
    def consultar_saldo(self):  # getter
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo

    # Método para sacar dinheiro da conta
    def sacar(self, value):
        if self._saldo < value:
            print("AVISO: Saldo insuficiente.")
            return
        self._saldo -= value

    # Maneira correta de definir um valor para um atributo protegido,
    # através de um método setter
    def depositar(self, value):  # setter
        self._saldo += value


# Instanciando e imprimindo informações de uma conta bancária
conta = Conta(cliente="Bruno")

conta._tipo_de_conta = 1000
conta.__id_interno = 567891

# Imprime todas as informações daquele objeto, seus métodos dunder e públicos
print(dir(conta))
print(conta.cliente)

# Realizando operações de maneira correta
# em cima do atributo protegido `_saldo`

print(conta.consultar_saldo())

conta.depositar(100)
conta.depositar(50)

print(conta.consultar_saldo())

conta.sacar(80)
print(conta.consultar_saldo())

conta.sacar(200)
