#!/usr/bin/env python3
"""Envio de e-mails utilizando interpolação e SMTP."""
__version__ = "0.1.1"
__license__ = "Unlicense"

# Importando biblioteca `os` e `sys`
import os
import sys

# Biblioteca padrão do Python para envio de emails com o protocolo SMTP
import smtplib

# Template de e-mail pronto
from email.mime.text import MIMEText

# Definindo as informações do servidor, host e port
SERVER = "localhost"
PORT = "8025"

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

# Abrindo uma instância de um servidor para envios de email com o protocolo SMTP.
# O `host` é o endereço do servidor e `port` é a porta TCP que vai receber os e-mails.
with smtplib.SMTP(host=SERVER, port=PORT) as server:

    # Iterando sobre cada linha do arquivo de emails
    # Ao utilizar o protocolo contains `in` em um arquivo com o `open()` o interpretador vai ler linha por linha do arquivo
    for line in open(filepath):

        # Desempacota os dados das linhas nas variáveis `name` e `email`
        name, email = line.split(",")
        text = (
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

        from_ = "geovannepadilha@hotmail.com"
        to = ", ".join([email])

        # Criando uma instância que vai armazenar os dados necessários para o envio do e-mail
        # usando o template MIMEText
        message = MIMEText(text)

        # Definindo o assunto, da onde e para onde vai enviado, com o modelo do MIMEText
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        # Enviando o email a partir do servidor já instanciado,
        # passando de quem e para quem vai ser enviado a mensagem, 
        # juntamente com a mesma sendo convertido para texto puro através do objeto MIMEText
        server.sendmail(from_, to, message.as_string())