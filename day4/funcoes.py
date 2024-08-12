#!/usr/bin/env python3
"""Exemplos de funções"""
__version__ = "0.1.0"
__license__ = "Unlicense"

"""
f(x) = 5 * (x / 2)
"""

# `Def`inindo uma função chamada `f` com um parâmetro `x`.
def f(x): # assinatura da função.
    # Cálculo da função.
    result = 5 * (x // 2)

    # Retorno explícito da função.
    return result 

# `Def`inindo uma função chamada `double` com um parâmetro `x`.
def double(x):
    # Retorno explícito da função.
    return x * 2

# Chamando a função e atribuindo seu retorno a uma variável.
valor = double(f(10))

# Comparando e exibindo o valor de retorno da função.
print(valor)
print(valor == 25)

####

# Definindo uma versão sem retorno explícito, mas sim retorno implícito de None.
# Função sem retorno é chamada de Procedimento/Procedure.
def print_in_upper(text):
    print(text.upper())

# Chamada da função
print_in_upper("giovanni")

####

# Definindo a função chamada `heron` com três parâmetros `a, b e c`.
def heron(a, b, c):
    """Cálcula a área de um triângulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c) 

    # Retorno explícito da função.
    return area ** 0.5 # math.sqrt(area)

# Lista de tuplas contendo os lados de triângulos.
triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

# Para cada triâgulo, chama a função `heron` e desempacote os valores da tupla como parâmetros.
for t in triangulos:
    area = heron(*t)
    print(f"A área do triângulo é: {area}")

####

# Definindo uma função sem parâmetro de assinatura vazia.
def nome_da_funcao():
    print("Hello função")

    # Retorno explícito.
    return 1

# Chamada da função atribuindo a uma variável e imprimindo-a.
result = nome_da_funcao()
print(result)