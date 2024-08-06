#!/usr/bin/env python3

nome = "Global"

def funcao():
    nome = "Local"
    print("Nome Local:", nome)

    # Maneira mais "adequada" de acessar uma variável global no meio do código de uma função.
    # Dessa forma não é necessário utilizar `global` no início, podendo alterar entre variáveis locais e
    # globais no código da função.
    nome = globals()["nome"]
    print("Nome Global:", nome)

funcao()