#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade usando dicionários

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"
__author__ = "Giovanni Padilha"

# Dicionário contendo todas as salas de aula da escola.
# Cada sala tem uma chave com o número da sala e uma lista com os alunos.
salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2": ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}

# Dicionário contendo todas as atividades extracurriculares.
# Cada atividade tem uma chave com o seu nome e uma lista com os alunos inscritos. 
atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]

}

# Itera sobre cada atividade.
# Transforma em tupla cada conjunto chave/valor do dicionário e desempacota em duas variáveis.
for nome_atividade, alunos_atividade in atividades.items():

    # Para cada atividade itera sobre todas as salas de aula da escola.
    # Segue o mesmo princípio de antes, converte para Tupla e desempacota em duas variáveis.
    for numero_sala, alunos_sala in salas.items():
        
        # Mensagem para mostrar a sala e a atividade do loop atual.
        print(f"Alunos da {numero_sala} na Atividade de {nome_atividade}")

        # Método para encontrar usando sets com a operação de Intersecção.
        # Mais performance O(1), preferível em casos que não possua mais de um aluno com o mesmo nome.
        #print(set(alunos_atividade).intersection(alunos_sala))

        # Método de iterar sobre cada aluno de cada atividade e verificar se está dentro da sala em questão.
        # Menos performance O(n), usar em casos que se possui mais de um aluno com o mesmo noem.
        for aluno_aula in alunos_atividade:
            if aluno_aula in alunos_sala:
                print("->", aluno_aula)

        # Divisor
        print("-" * 40)