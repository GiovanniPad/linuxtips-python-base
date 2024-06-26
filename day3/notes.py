#!/usr/bin/env python3
"""Bloco de notas

$ python3 notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia.

$ python3 notes.py read tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Importando bibliotecas `os` e `sys`
import os
import sys

# Coletando o caminho relativo do diretório atual
path = os.curdir

# Definindo o caminho relativo do arquivo para armazenar as notas
filepath = os.path.join(path, "archives", "notes.txt")

# Coletando os argumentos CLI, menos o nome do arquivo.py
arguments = sys.argv[1:]

# Lista com os comandos aceitos
valid_commands = ("new", "read")

# Verificando se a lista de argumentos está vazia
# Se não estiver com conteúdo, imprime uma mensagem de erro, juntamente com os comandos válidos e encerra o programa
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand {valid_commands}")
    sys.exit(1)

# Verifica se o comando inserido pelo usuário está dentro dos comandos válidos

# Se não estiver dentro, imprime um erro juntamente com o comando errado e encerra o programa
if arguments[0] not in valid_commands:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)

# Verifica se o comando inserido é o `new`, comando para criar uma nova nota
if arguments[0] == "new":

    # Coleta o título da nota dos argumentos CLI
    title = arguments[1] # TODO: Tratar exception

    # Cria uma lista que armazena o título, tag e o conteúdo da nota em cada posição
    note = [
        f"{title}",

        # Inserção de dado, excluindo os espaços em branco do início e do fim
        input("tag: ").strip(),
        input("text:\n").strip()
    ]

    # Abre o arquivo com o Gerenciador de Contexto `with` para armazenar a nota
    with open(filepath, "a") as file_:

        # A função `join(list)` concatena uma lista de strings em uma única string, inserindo um tab (`\t`) entre cada item 
        # e no final um espaço em branco (`\n`)
        # Por fim, a string concatena é escrita em uma única linha no arquivo
        file_.write(f"\t".join(note) + "\n")

# Verifica se o comando inserido é o `read`, comando para ler notas a partir da tag
if arguments[0] == "read":

    # Itera sobre cada linha do arquivo
    for line in open(filepath):

        # Desempacota a linha dividida por tab (`\t`) do arquivo em três variáveis, 
        # o primeiro valor é título, segundo valor a tag e o terceiro valor o conteúdo da nota
        title, tag, text = line.split("\t")

        # Compara a tag de cada linha com a tag inserida pelo usuário
        # Na tag inserida pelo usuário, a função `strip()` retira os espaços em branco do início e do fim da string e
        # a função `lower()` transforma todas os caracteres da string em minúsculo

        # Na tag da nota apenas é usada a função `lower()` que transforma todos os caracteres da string em minúsculo
        if tag.lower() == arguments[1].strip().lower():

            # Imprime o título, tag e o conteúdo da nota separados por linhas
            print(f"Title: {title}")
            print(f"Tag: {tag}")
            
            # Não coloca uma quebra de linha no final
            print(f"Text: {text}", end="")
            print("-" * 50)
