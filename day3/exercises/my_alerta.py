"""Alarme de temperatura.

Faça um script que pergunta ao usuário qual a temperatura atual e o índice de umidade do ar
sendo que será exibida uma mensagem de alerta dependendo das condições:

Se temp maior 45: ALERTA!!! Perigo calor extremo
Senão, temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
.. temp entre 10 e 30: Normal
.. temp entre 0 e 10: Frio
.. temp < 0: ALERTA: Frio extremo
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

import logging

log = logging.Logger("alerta.py", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Minha solução

while True:
    try:
        temp = float(input("temperatura:"))
        moisture = float(input("umidade:"))
    except ValueError:
        log.error("Valor inserido inválido")
        continue
    break

if temp > 45:
    print("ALERTA!!! Perigo calor extremo")
elif (temp * 3) >= moisture:
    print("ALERTA!!! Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("Normal")
elif temp >= 0 and temp < 10:
    print("Frio")
else:
    print("ALERTA!!! Frio extremo")