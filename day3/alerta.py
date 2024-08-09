#!/usr/bin/env python3
"""Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o índice de umidade do ar
sendo que será exibida uma mensagem de alerta dependendo das condições:

Se temp maior 45: ALERTA!!! Perigo calor extremo
Senão, temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
.. temp entre 10 e 30: Normal
.. temp entre 0 e 10: Frio
.. temp < 0: ALERTA: Frio extremo
"""
__version__ = "0.1.1"
__author__ = "Giovanni Padilha"

import logging
import sys

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



# Solução do professor

# TODO: Mover para módulo de utilidades.

# Função que verifica se a lista de inputs já foi totalmente preenchida.
# Retorna um bool, True caso ela estiver cheia, senão False.
def is_completely_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
    )
    return info_size == filled_size

# Função que pede ao usuário para inserir as informações para cada input
# no dicionário de informações necessárias.
def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""

    # Sempre evitar de iterar e alterar um objeto mutável em um loop, para isso utilizar sempre outro objeto para iterar.
    # Ao usar `keys()` é criado um objeto do tipo lista contendo as chaves do dicionário e a partir desse objeto "imagem" iteramos no dicionário,
    # evitando assim erros de Runtime, onde se itera e altera o mesmo objeto.
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = float(input(f"{key}:").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

# Dicionário contendo as informações necessárias.
info = {
    "temperatura": None,
    "umidade": None
}

# Loop while, executa enquanto a função `is_completely_filled` retornar True, negando, False.
while not is_completely_filled(info):

    # Função que coleta as informações do usuário.
    read_inputs_for_dict(info)

temp, umidade = info.values()

# Ifs e elifs para verificar as condicionais e exibir a mensagem correta para cada condicional.
if temp > 45:
    print("ALERTA!!! Perigo calor extremo")
elif (temp * 3) >= umidade:
    print("ALERTA!!! Perigo calor úmido")
elif temp >= 10 and temp <= 30:
#elif temp in range(10, 31):
    print("Normal")
elif temp >= 0 and temp < 10:
    print("Frio")
elif temp < 0:
    print("ALERTA!!! Frio extremo")