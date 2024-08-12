#!/usr/bin/env python3
"""Exemplos dos escopos global e local."""
__version__ = "0.1.0"
__license__ = "Unlicense"

contador = 0

def incrementa_contador():
    # ... começa o escopo local

    # Força a função acessar determina variável do escopo global.
    # Sempre usar no início do escopo, senão usar dará erro, pois
    # o python não realiza de atribuição em variáveis de diferentes escopos.
    global contador
    contador += 1

incrementa_contador()
incrementa_contador()
incrementa_contador()
incrementa_contador()

print(contador)