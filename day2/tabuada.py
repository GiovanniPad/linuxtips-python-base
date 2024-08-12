#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Exemplo:

---Tabuada do 1---
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3

##################

---Tabuada do 2---
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6

##################

...
"""
__version__ = "0.1.0"
__license__ = "Unlicense"

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
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)