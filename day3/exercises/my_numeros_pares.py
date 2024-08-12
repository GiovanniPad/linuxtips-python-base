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
__author__ = "Giovanni Padilha"

# Minha solução

# Enquanto o número for menor e igual a 200 imprimir apenas os números pares e somar na variável de controle.
num = 1
while num <= 200:
    if num % 2 == 0:
        print(num)
        num += 1
        continue
    num += 1