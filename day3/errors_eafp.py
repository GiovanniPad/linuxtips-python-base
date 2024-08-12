#!/usr/bin/env python3
"""Abordagem EAFP para tratamento de erros em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

import logging
import time

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

# Função para tentar um arquivo, caso não seja possível ela tenta novamente uma vez.
# O argumento `retry` indica a quantidade de vezes que será refeita a operação de abrir um arquivo qualquer.
# O retry é feito usando recursão. E retorna uma lista vazia no final.
def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""   

    # Verifica se o argumento `retry` tem seu valor mais que 999 para impedir de
    # realizar uma recursão de 1000 chamadas.
    if retry > 999:
        raise ValueError("Retry cannot be above 999.")
    
    # RETRY COM RECURSÃO.

    # Bloco `try` que se espera um erro.
    try:
        # Retorna todas as linhas do arquivo.
        return open(filepath).readlines()

    # Captura a exceção de arquivo não localizado, imprimindo a mensagem de erro e encerrando o programa.
    except FileNotFoundError as e:
        
        # Log do tipo error, exibe a mensagem de erro da exceção capturada.
        log.error("%s", e)
        time.sleep(2)
        if retry > 1:
            
            # A função, após estourar uma Exception, chama ela mesma para realizar o retry,
            # passando como parãmetro a quantia de retry menos 1, para que o próximo retry seja realizado.
            # OBS: não pode realizar mais de 1000 chamadas em sequência usando recursão e é obrigatório usar um return,
            # para que o valor possa ser acessado na chamada da função.

            return try_to_open_a_file(filepath, retry=retry - 1)

    # Bloco `else`, se não ocorrer nenhum erro ele vai ser executado.
    else:
        print("Sucesso!!!")

    # Bloco `finally`, vai ser executado sempre, independente se ocorrer erro ou não.
    finally:
        print("Execute isso sempre!")

    # RETRY COM FOR

    #for attempt in range(1, retry + 1):
        # Bloco `try` que se espera um erro
        #try:
            #return open(filepath).readlines()
        # Captura a exceção de arquivo não localizado, imprimindo a mensagem de erro e encerrando o programa.
        #except FileNotFoundError as e:
            # Log do tipo error, exibe a mensagem de erro da exceção capturada.
            #log.error("%s", e)
            #time.sleep(2)
        # Bloco `else`, se não ocorrer nenhum erro ele vai ser executado.
        #else:
            #print("Sucesso!!!")
        # Bloco `finally`, vai ser executado sempre, independente se ocorrer erro ou não.
        #finally:
            #print("Execute isso sempre!")
            
    return []

# Caso abrir o arquivo com sucesso, imprime cada linha contida no arquivo.
for line in try_to_open_a_file("archives/names.txt", retry=5):
    print(line)