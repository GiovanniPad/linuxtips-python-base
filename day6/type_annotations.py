#!/usr/bin/env python3

# Classe do módulo `decimal` que permite trabalhar com valores mais precisos
from decimal import Decimal
# Classes do módulo `typing` que permite usar Type Annotations
# antes do Python 3.9
from typing import Set, Optional
# Decorator do módulo `dataclasses` que permite utilizar Type Annotations
# para criar inicializadores de classes
from dataclasses import dataclass


# Type Annotations antes do Python 3.9
def function(arg: Optional[Set[int]]):
    ...


# Type Annotations após o Python 3.9
def function2(arg: set[int] | None):
    ...


# Carrinho de compras

# Definindo as variáveis
produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5
cliente_especial = True


# Função que calcula o total da compra
# Definindo os tipos de cada parâmetro e do retorno da função
# através do Type Annotation
def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade


# Aplicando desconto, pode gerar um bug, caso definir um número sem o Decimal
# Podendo virar um Float sem se perceber
if cliente_especial:
    valor = Decimal(4.3)

# Calcula o total
total = calcula_total(valor, quantidade)

# Imprime o resultado
print("Tipo:", type(total))
print(f"O total é R${total:.2f}")


# Decorator `@dataclass` que utiliza os Type Annotations dos atributos
# da classe para criar um inicializador de classe `__init__`
@dataclass
class Pessoa:
    pk: str
    name: str
    points: int = 100


# Usando a própria função como um Type Annotation,
# permitindo verificar tanto o tipo da instância quanto os tipos dos atributos
def funcao(dados: Pessoa):
    ...


# Instanciando a classe Pessoa, já verificando seus tipos ao instanciar
dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)

# Passando a instância para função, não gerando nenhum problema
funcao(dados)
