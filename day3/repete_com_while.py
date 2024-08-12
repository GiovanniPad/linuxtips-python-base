#!/usr/bin/env python3
"""Exemplos de uso da estrutura de repetição while do Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Loop while, ocorre enquanto a condição de parada for Verdadeira (True)
n = 0
while n < 101: # loop infinito, main loop
    if n >= 40 and n <= 60:
        n += 1
        continue

    print(n)
    n += 1