#!/usr/bin/env python3

import sys
import logging

# LBYL - Look Before You Leap
# Primeiro você verifica se é possível uma operação.
"""
# Verifica se o caminho existe
if os.path.exists("archives/names.txt"):

    # Problema de Race Condition que pode ocorrer ao usar LBYL
    input("...")

    # Lê as linhas do arquivo e retorna uma lista com cada linha sendo uma posição
    names = open("archives/names.txt").readlines()
else:

    # Mensagem de erro caso o arquivo não existir e encerra o programa
    print("[Error] File names.txt not found.")
    sys.exit(1)

# Verifica se o tamanho da lista é maior ou igual a 3
# pois para acessar o terceiro elemento, a lista precisa ter o tamanho 3
if len(names) >= 3:
    print(names[2])
else:
    # Mensagem de erro caso a lista não tiver 3 ou mais elementos
    print("[Error] Missing name in the list")
    sys.exit(1)
"""

# Criando um Logger e Handler específicos para tratar as mensagens de erro desse script.
log = logging.Logger("errors.py", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# EAFP - (Easy to Ask Forgiveness than Permission)
# Primeiro executa, depois trata os erros/exceções.

# A palavra dedicada `try` delimita um bloco de código onde o código vai executado pelo menos uma vez,
# bloco onde é esperado algum erro.
try:
    # "Estourando" uma exceção própria
    raise RuntimeError("Ocorreu um erro")

# Bloco onde a exceção é capturada, sendo possível usar a variável `e` para mostrar sua mensagem.
except Exception as e:
    # Log do tipo warning, exemplo
    log.warning(str(e))

# Bloco `try` que se espera um erro
try:
    names = open("archives/names.txt").readlines()

# Captura a exceção de arquivo não localizado, imprimindo a mensagem de erro e encerrando o programa.
except FileNotFoundError as e:
    
    # Log do tipo error, exibe a mensagem de erro da exceção capturada.
    log.error(str(e))
    sys.exit(1)
    # TODO: Usar retry

# Bloco `else`, se não ocorrer nenhum erro ele vai ser executado.
else:
    print("Sucesso!!!")

# Bloco `finally`, vai ser executado sempre, independente se ocorrer erro ou não.
finally:
    print("Execute isso sempre!")

# Segue a mesma lógica
try:
    print(names[5])

# Esse é o bloco de Bare Except, ele vai coletar todo e qualquer tipo de erro
# que ocorrer no bloco `try`.
except:

    # Log do tipo error, mostrando uma mensagem (atributo `message`) personalizada.
    log.error(
        "Missing name in the list, please use index in a range of %d",
        len(names)
    )
    sys.exit(1)