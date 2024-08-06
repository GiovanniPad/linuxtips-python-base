#!/usr/bin/env python3

def transforma_em_maisculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2

# função principal
def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)

names = ["Bruno", "João", "Bernardo", "Cintia", "Marcia", "Juca"]

# Imprime a lista de nomes ordenada em ordem alfabética e no tamanho de cada nome.
print(sorted(names, key=len))

# Imprime a lista de nomes ordenada em ordem alfabética e utiliza uma função
# lambda para ordenar pela quantidade de letras "i" encontradas em cada nome.
print(sorted(names, key=lambda name: name.count("i")))

# Filtra da lista de nomes, apenas os nomes que começam com "b",
# para isso é utilizada uma função lambda e depois converte para lista.
print(list(filter(lambda name: name[0].lower() == "b", names)))

# Aplica uma função lambda que adiciona o texto "Hello + nome" para cada
# nome da lista de nomes e depois converte para uma lista.
print(list(map(lambda name: "Hello " + name, names)))

# Calculadora com lambdas

# Entrada do tipo da operação e os números
operation = input("operation [sum, sub, mul, div]: ").strip()
n1 = input("n1:").strip()
n2 = input("n2:").strip()

# Definindo as operações dentro de um dicionário utilizando funções lambdas,
# onde cada função lambda executa uma operação matemática básica.
operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a // b,
}

# Acessando o dicionário de operações utilizando como chave a operação que
# o usuário inseriu e executando o valor naquela chave como uma função, passando
# os números 1 e 2 como argumentos.
print(f"O resultado é: {operations[operation](int(n1), int(n2))}")