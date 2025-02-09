#!/usr/bin/env python3

# Biblioteca para manipular o banco de dados SQLite
import sqlite3
# Biblioteca para utilizar caminhos de arquivos e pastas
from pathlib import Path

# Definindo o caminho do arquivo do banco de dados SQLite
database_path = Path(".", "day7", "archives", "db_example.db")

# Abrindo uma conexão com o banco / criando o arquivo
con = sqlite3.connect(database_path)

# Executando um comando para habilitar chaves estrangeiras,
# ou seja, relacionamentos entre tabelas
con.execute("PRAGMA foreign_keys = ON;")

# Instruções SQL para criação das tabelas do banco de dados
# instructions = """\
# CREATE TABLE if not exists person (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     name varchar NOT NULL,
#     email varchar UNIQUE NOT NULL,
#     dept varchar NOT NULL,
#     role varchar NOT NULL
# );
# ---
# CREATE TABLE if not exists balance (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     person integer UNIQUE NOT NULL,
#     value integer NOT NULL,
#     FOREIGN KEY(person) REFERENCES person(id)
# );
# ---
# CREATE TABLE if not exists movement (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     person integer NOT NULL,
#     value integer NOT NULL,
#     date datetime NOT NULL,
#     actor varchar NOT NULL,
#     FOREIGN KEY(person) REFERENCES person(id)
# );
# ---
# CREATE TABLE if not exists user (
#     id integer PRIMARY KEY AUTOINCREMENT,
#     person integer UNIQUE NOT NULL,
#     password varchar NOT NULL,
#     FOREIGN KEY(person) REFERENCES person(id)
# );
# """

# Iterando sobre as instruções para executar uma por vez
# for instruction in instructions.split("---"):
#     con.execute(instruction)

# Instrução para inserir um registro na tabela `person`
# instruction = """\
# INSERT INTO person (name, email, dept, role)
# VALUES ('Karla', 'karla@rocha.com', 'Sales', 'Manager');
# """

# Executando o comando SQL
# con.execute(instruction)

# Confirmando o comando SQL
# con.commit()

# Instrução para seleção JOIN de pessoas e seus saldos
instruction = """\
SELECT person.name, person.email, balance.value
FROM person
LEFT JOIN balance
WHERE person.id = balance.person;
"""

# Definindo um cursor (ponteiro), necessária para selecionar
# registros das tabelas do banco de dados
cur = con.cursor()

# Coletando os resultados da query de seleção
# Retorna um Cursor Object
result = cur.execute(instruction)

# Confirmando a instrução de seleção
con.commit()

# Para cada linha no resultado da query de seleção
# Cada linha é um registro e seu formato é de uma tupla
for row in result:
    # Insere um novo saldo para cada usuário na tabela `balance`
    # O uso do caractere "?" indica um placeholder para receber dados,
    # espera-se uma tupla ou uma lista
    # instruction = "INSERT INTO balance (person, value) VALUES (?, ?)"

    # Passa a instrução e os parâmetros (dados) que vão ser inseridos nos
    # placeholders, de acordo com a ordem da tupla/lista
    # con.execute(instruction, row)

    # Confirmando cada inserção na tabela `balance`
    # con.commit()

    # Imprimindo as linhas do resultado da consulta
    print(row)
