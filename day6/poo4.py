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

# Propriedades


# Classe que representa uma conta bancária
class Conta:
    # Atributo protegido / protected
    _tipo_de_conta = "corrente"
    # Atributo privado / private
    __id_interno = 456789

    # Método inicializador da classe
    def __init__(self, cliente):
        self.cliente = cliente
        self.__saldo = 0

    # Declara que o atributo `saldo` é uma propriedade,
    # esse decorator declara um método getter, que retorna o valor
    # de `saldo`
    @property  # getter, consulta o atributo
    def saldo(self):
        if self.__saldo < 0:
            print("AVISO: você está devendo")
        return self.__saldo

    # Propriedade que declara um setter para o atributo `saldo`,
    # tornando-o possível alterar seu valor
    @saldo.setter  # setter, atribui ao atributo
    def saldo(self, value):
        self.__saldo += value

    # Propriedade que declara um deleter para o atributo `saldo`,
    # tornando possível resetar o valor de `saldo` ao executá-lo
    @saldo.deleter
    def saldo(self):
        self.__saldo = 0


# Instanciando e imprimindo informações de uma conta bancária
conta = Conta(cliente="Bruno")

print(conta.cliente)
# Utilizando o método getter para coletar o valor do atributo `saldo`
print(conta.saldo)

# Utilizando o método setter para alterar o valor do atributo `saldo`
conta.saldo = 100
print(conta.saldo)

conta.saldo = -50
print(conta.saldo)

# Reiniciando o valor do atributo `saldo` através do método deleter,
# para invocar esse método usa a palavra reservada `del`
del conta.saldo

print(conta.saldo)
