#!/usr/bin/env python3
"""Envio de e-mail com mailtrap.io"""
import smtplib
from email.mime.text import MIMEText

SERVER = "sandbox.smtp.mailtrap.io"
PORT = 2525

from_ = "Private Person <from@example.com>"
to = ["A Test User <to@example.com>"]
subject = "Teste mailtrap.io"
text = """\
<html>
    Envio de e-mail usando o servidor mailtrap.io
    <br>
    <b>Olá, Mundo!</b>
</html>
"""

message = MIMEText(text, "html")

message["From"] = from_
message["To"] = ", ".join(to)
message["Subject"] = subject

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.login(user="6e708a60b21271", password="e02467786ecd39")
    server.sendmail(from_, to, message.as_string())
    print("E-mail enviado com sucesso!")