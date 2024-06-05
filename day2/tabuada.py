#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Exemplo:

Tabuada do 1
1
2
3
...
-------------
Tabuada do 2
2
4
6
...
-------------
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Cria uma lista, sempre usando `[]`
#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
Função `range()` retorna uma lista de números.
    - O último valor do range sempre deve ser acrescido de 1, pois o range é não inclusivo.
    - O próprio objeto range é um tipo de dado, um gerador de dados do Python.

Função `list()` converte o objeto range para uma lista.
"""
numeros = list(range(1, 11))

"""
Objetos Python que implementam o protocolo Iterable, podem ser iterados/percorríveis.
Para trabalhar com iteráveis no Python utiliza a palavra reservada `for`.

Para cada numero em numeros:
"""
for numero in numeros:
    # O caractere `,` podem concatenar strings e números juntos.
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------")