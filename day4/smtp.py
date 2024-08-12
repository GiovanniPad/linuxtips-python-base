#!/usr/bin/env python3
"""Exemplo de envio de e-mail em Python usando a biblioteca smtplib."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Biblioteca responsável pelo envio de e-mails no formato SMTP
import smtplib

# Definindo o `host` e a `port` usados pelo servidor para o envio do e-mail.
SERVER = "localhost"
PORT = 8025

# Definindo a estrutura de um email, contendo o remetente, destinatário, assunto e mensagem do e-mail.
# O To (Destinatário) deve ser uma lista de e-mails, mesmo que haja apenas um.
# Pode ser usado tags HTML na mensagem, caso o servidor que vai receber aceite tags HTML.
FROM = "geovannepadilha@hotmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá, Mundo!</b>
"""

# Mensagem construída usando o padrão SMTP,
# obrigatoriamente a primeira linha não deve ser vazia, por isso usa `\` para evitar a quebra de linha.
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

# Criando uma instância de servidor local para envio dos e-mails, 
# com o host e a port estabelecidas anteriormente.

# Para abrir um servidor local para testes de e-mails SMTP usar o comando
# normal: `python3 -m aiosmtpd -n`
# debug: `python3 -m aiossmtpd -nd`

with smtplib.SMTP(host=SERVER, port=PORT) as server:

    # Enviando o e-mail.
    server.sendmail(FROM, TO, message.encode("utf-8"))