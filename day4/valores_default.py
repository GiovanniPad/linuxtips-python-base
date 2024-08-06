#!/usr/bin/env python3

import time

# Definindo um valor padrão para o argumento `sobrenome` caso nenhum
# argumento for passado ao chamar a função, caso passar, ele será sobrescrito.
def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: ..., sobrenome: ... ou "Sabugosa"}
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Bruno", "Rocha")
imprime_nome("Linus")

# Criando um valor padrão (default) para o argumento `timeout`.
def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range (1, timeout + 1):

        # Função para criar um "delay" na execução do código. Como um carregamento.
        time.sleep(1)
        print("." * i)
    print("erro ao conectar")

conecta("localhost")