#!/usr/bin/env python3

# Importando biblioteca `os` e `sys`
import os
import sys

# Coletando os argumentos CLI necessários, excluindo o nome do arquivo.py
arguments = sys.argv[1:]

# Verificando se a lista de argumentos não está vazia
# Se estiver, imprime um erro e encerra o programa
if not arguments:
    print("Informe o nome do arquivo de emails e o template de email")
    sys.exit(1)

# Definindo o nome do arquivo de emails e de template
filename = arguments[0]
templatename = arguments[1]

# Coletando o caminho relativo do diretório atual
path = os.curdir

# Unindo os caminhos dos diretórios juntamente com o nome do arquivo de emails e tempalte
filepath = os.path.join(path, "archives", filename)
templatepath = os.path.join(path, "archives", templatename)

# Iterando sobre cada linha do arquivo de emails
# Ao utilizar o protocolo contains `in` em um arquivo com o `open()` o interpretador vai ler linha por linha do arquivo
for line in open(filepath):

    # Desempacota os dados das linhas nas variáveis `name` e `email`
    name, email = line.split(",")

    # TODO: Substituir por envio de email

    # Imprime cada mensagem do email, juntamente do email do destinatário
    print(f"Enviando email para: {email}")
    print(
        # Lê o arquivo de template e coleta o template de emails e utiliza da interpolação `%` para inserir os dados
        open(templatepath).read() 
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escreve muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 5,
            "preco": 50.5,
        }
    )

    # Divisor
    print("-" * 50)