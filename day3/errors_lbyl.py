#!/usr/bin/env python3
"""Abordagem LBYL para tratamento de erros em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

import sys
import os

# LBYL - Look Before You Leap
# Primeiro você verifica se é possível uma operação.

# Verifica se o caminho existe
if os.path.exists("archives/names.txt"):

    # Problema de Race Condition que pode ocorrer ao usar LBYL
    input("...")

    # Lê as linhas do arquivo e retorna uma lista com cada linha sendo uma posição
    names = open("archives/names.txt").readlines()
else:

    # Mensagem de erro caso o arquivo não existir e encerra o programa
    print("[Error] File names.txt not found.")
    sys.exit(1)

# Verifica se o tamanho da lista é maior ou igual a 3
# pois para acessar o terceiro elemento, a lista precisa ter o tamanho 3
if len(names) >= 3:
    print(names[2])
else:
    # Mensagem de erro caso a lista não tiver 3 ou mais elementos
    print("[Error] Missing name in the list")
    sys.exit(1)
