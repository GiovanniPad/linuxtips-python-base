#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200

ex 
`python3 numeros_pares.py`
2
4
6
8
...
"""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Soluçao do professor

# Para cada número em um objeto ´range´ entre 1 e 200 imprimir apenas os números pares
for num in range(1, 201):
    if num % 2 == 0:
        print(num)
        continue