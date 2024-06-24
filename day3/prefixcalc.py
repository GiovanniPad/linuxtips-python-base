#!/bin/usr/env python3
"""Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ python3 prefixcalc.py sum 5 2
7

$ python3 prefixcalc.py mul 10 5
50

$ python3 prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

import sys

# Colentando os argumentos necessários
arguments = sys.argv[1:]

# TODO: Exceptions
# Verificando se a lista de argumentos está vazio ou não.
# Se estiver vazia, perguntar a operação e os números ao usuário e reatribui na variável `arguments`.

# Uma lista vazia ao ser passada em um statement, retorna False. Com o uso do not, inverte, ficando como True.
if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")

    arguments = [operation, n1, n2]

# Verifica se a lista de argumentos tem menos de 3 argumentos.
# Se tiver, imprime um erro, junto com um exemplo de uso e encerra o programa.
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

# Desempacota a variável `arguments` em uma variável com a operação e uma com os números.
operation, *nums = arguments

# Tupla com as operações válidas.
valid_operations = ("sum", "sub", "mul", "div")

# Verifica se a operação digitada pelo usuário não está dentro das operações válidas.
# Se não estiver, imprime um erro, junto com a lista de operações válidas e encerra o programa.
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

# Lista para armazenar os números validados.
validated_nums = []

# Validando cada um dos números inseridos pelo usuário.
for num in nums:
    # TODO: Repetição com while + exceptions

    # Remove, se houver, o "." no conteúdo da variável.
    # Após, verifica se o conteúdo possui apenas dígitos.

    # Se não tiver apenas dígitos, imprime um erro, junto com o conteúdo da variável em questão e encerra o programa.
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)

    # Verifica se no conteúdo da variável possui o "."

    # Se possuir, converter para float.
    # Se não possuir, converter para int.
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    # Insere o número já validado dentro da Lista de números validados.
    validated_nums.append(num)

# Desempacota os números validados nas variáveis `n1` e `n2`.
n1, n2 = validated_nums

# Variável para armazenar o resultado.
result = 0

# TODO: Usar dict de funções

# Verifica qual o tipo da operação, realizando-a e armazenando o resultado na variável `result`.
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":

    # Verifica se o dividor é igual a 0, não é possível dividir por 0.

    # Se for igual, imprime uma mensagem de erro e encerra o programa.
    if n2 == 0:
        print("Division by zero")
        sys.exit(1)
    result = n1 / n2

# Imprime o resultado na tela.
print(f"O resultado é {result}")