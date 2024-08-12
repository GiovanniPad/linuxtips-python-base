#!/usr/bin/env python3
"""Exemplos da anatomia das funções em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Sphinx docstring
def nome_da_funcao(a, b, c):
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parâmetro a tiver o valor 10 vai
    acontecer x.

    >>> nome_da_funcao(1, 2, 3)
    6
    
    :param a: Número inteiro
    :type a: int
    :param b: Número inteiro
    :type b: int
    :param c: Número inteiro   
    :type c: int 
    :return: Retorna o resultado de a + b + c
    :rtype: int
    """
    resultado = a + b + c
    return resultado

# Type hints docstring
def nome_da_funcao2(a: int, b: int, c: int) -> int:
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parâmetro a tiver o valor 10 vai
    acontecer x.

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# Passagem de argumentos posicionais
valor = nome_da_funcao2(1, 2, 3)

# Passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(b=1, c=2, a=3)

# Passagem de argumentos mista
valor = nome_da_funcao(1, c=2, b=3)

print(valor)

#################################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""

    # Tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(valor1, valor2, valor3)

#################################

# Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de 2 números."""
    return n1 + n2

# Normal
print(soma(10, 20))

# Argumentos em sequência / posicional
args = (20, 30) # tuple, list, string
#print(soma(args[0], args[1]))
print(soma(*args))

# Argumentos dicionário / nomeados
args = {"n2": 90, "n1": 100} # dict, hashmap
#print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
    (5, 10),
    [8, 13],
]

for item in lista_de_valores_para_somar:
    # Verifica se a variável é do tipo dict,
    # se for dict usa o desempacotamento com dois asterísticos
    # senão usa o desempacotamento com um arterístico.
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))