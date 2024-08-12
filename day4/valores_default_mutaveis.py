#!/usr/bin/env python3
"""Exemplos do uso de valores default mutáveis em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# set, dict, list

# A cada chamada da função é criada uma nova lista, caso contrário,
# todas as chamadas da mesma função irão acessar e modificar o mesmo objeto.
def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

adiciona_a_lista(4, [])
adiciona_a_lista(5, [])
print(adiciona_a_lista(6, []))