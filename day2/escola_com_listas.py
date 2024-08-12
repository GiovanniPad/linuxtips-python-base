#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade usando listas.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Listas com alunos
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# Listas com alunos inscritos nas atividades.
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Cria uma Lista atribuindo cada Lista de aula e label em uma Tupla.
atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Itera sobre cada atividade da Lista de atividades.
# Desempacota a Tupla, atribuindo o label da atividade para a variável `nome_atividade` e os alunos para `alunos_atividade`.
for nome_atividade, alunos_atividade in atividades:
    print(f"Alunos da atividade de {nome_atividade}\n")

    # Variáveis para adicionar os alunos de cada sala de determinada atividade.
    # Essas variáveis são resetadas a cada loop.
    atividade_sala1 = []
    atividade_sala2 = []

    # Iterando cada aluno de cada atividade.
    # Complexidade O(n).
    for aluno in alunos_atividade:
        
        # Comparando se o aluno da atividade está na sala 1 ou sala 2.
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    
    # Imprimindo os alunos de cada sala.
    print("Sala 1:", atividade_sala1)
    print("Sala 2:", atividade_sala2)
    print("-" * 20)