#!/usr/bin/env python3

# Coleção materializada
#numbers = [1, 2, 3, 4, 5, 6]

# start, next, stop e step
numbers = range(1, 11)

# For loops / Laço for

# Para cada número em um range de números, imprima apenas os números pares, senão, pular para a próxima iteração.
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue

# -------------------------------------------------------

# Programação imperativa, linha a linha
original = [1, 2, 3]
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Programação Funcional
# List Comprehension, mesma função do loop for acima, a diferença é que é feita apenas em uma linha.
dobrada = [n * 2 for n in original]
print(dobrada)

# ------------------------------------------------------

# Para cada linha em um arquivo, ler e armazenar a tag (key) e o valor dela em um dicionário.
dados= {}
for line in open("archives/post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
print(dados)

# Dict Comprehension
# Funciona da mesma forma que a List Comprehension.
# Mesma função do loop for acima
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("archives/post.txt") 
    if ":" in line
}
print(dados)