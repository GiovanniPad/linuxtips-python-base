#!/usr/bin/env python3
"""Exemplos de uso de parâmetros coringas em funções."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Define parâmetros coringas, que podem consumir qualquer tipo e quantia
# de valores passados na chamada da função.
# Usar `*` para consumir argumentos posicionais e `**` para argumentos nomeados.
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)
    print(f"timeout: {timeout}")

funcao("Bruno", 1, True, [], timeout=90, nome="João", cidade="Viana", data="hoje")
