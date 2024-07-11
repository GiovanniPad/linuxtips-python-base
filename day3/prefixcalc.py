#!/bin/usr/env python3
"""Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ python3 prefixcalc.py sum 5 2
7

$ python3 prefixcalc.py mul 10 5
50

$ python3 prefixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em infixcalc.log
"""
__version__ = "0.1.1"
__author__ = "Giovanni Padilha"

# Biblioteca que interage com o Sistema Operacional.
import os
# Biblioteca que interage com o ambiente de execução do interpretador Python.
import sys
# Biblioteca responsável por logs.
import logging
# Importando o módulo `datetime` da lib `datetime`, usado para coletar e modificar o dia e a hora.
from datetime import datetime

# Definindo um Logger e StreamHandler para imprimir as mensagens de erro deste script.
log = logging.Logger("prefixcalc.py", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Colentando os argumentos necessários
arguments = sys.argv[1:]

# Verificando se a lista de argumentos está vazio ou não.
# Se estiver vazia, perguntar a operação e os números ao usuário e reatribui na variável `arguments`.

# Uma lista vazia ao ser passada em um statement, retorna False. Com o uso do not, inverte, ficando como True.
if not arguments:
    
    # Função `input()` permite a inserção de informações pelo stdin da aplicação
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")

    arguments = [operation, n1, n2]

# Verifica se a lista de argumentos tem menos de 3 argumentos.
# Se tiver, imprime um erro, junto com um exemplo de uso e encerra o programa.
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")

    # Encerra a execução do programa com o código de erro 1
    sys.exit(1)

# Desempacota a variável `arguments` em uma variável com a operação e uma com os números.
operation, *nums = arguments

# Tupla com as operações válidas.
valid_operations = ("sum", "sub", "mul", "div")

# Verifica se a operação digitada pelo usuário não está dentro das operações válidas.
# Se não estiver, imprime um erro, junto com a lista de operações válidas e encerra o programa.
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

# Lista para armazenar os números validados.
validated_nums = []

# Validando cada um dos números inseridos pelo usuário.
for num in nums:
    # TODO: Repetição com while + exceptions

    # Remove, se houver, o "." no conteúdo da variável.
    # Após, verifica se o conteúdo possui apenas dígitos.

    # Se não tiver apenas dígitos, imprime um erro, junto com o conteúdo da variável em questão e encerra o programa.
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)

    # Verifica se no conteúdo da variável possui o "."

    # Se possuir, converter para float.
    # Se não possuir, converter para int.
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    # Insere o número já validado dentro da Lista de números validados.
    validated_nums.append(num)

# Bloco `try` a ser executado que se espera um erro.
try:
    # Desempacota os números validados nas variáveis `n1` e `n2`.
    n1, n2 = validated_nums

# Captura um erro do tipo valor e imprime sua mensagem e encerra o programa.
# Esse erro é estourado caso o tamanho da variável a ser desempacotada seja diferente de 2.
except ValueError as e:

    # Log do tipo error, com a mensagem capturada da exceção ValueError.
    log.error(str(e))
    sys.exit(1)

# Variável para armazenar o resultado.
result = 0

# TODO: Usar dict de funções

# Verifica qual o tipo da operação, realizando-a e armazenando o resultado na variável `result`.
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":

    # Verifica se o dividor é igual a 0, não é possível dividir por 0.

    # Se for igual, imprime uma mensagem de erro e encerra o programa.
    if n2 == 0:
        print("Division by zero")
        sys.exit(1)
    result = n1 / n2

# Coletando o caminho relativo do diretório atual
path = os.curdir

# Unindo e definindo o caminho do arquivo usado para armazenar as operações
filepath = os.path.join(path, "archives", "prefixcalc.txt")

# Definindo o dia e o horário da execução da operação através do objeto datetime
# Função `now()` retorna o dia, mês, ano e horário atuais
# Função `isoformat()` converte o conteúdo de retorno da função `now()` para um formato ISO legível
timestamp = datetime.now().isoformat()

# Coleta através de uma variável de ambiente o nome do usuário que executou a operação
user = os.getenv("USER", "anonymous")

# Bloco de código onde se espera um erro.
try:
    # Abre o arquivo de gravação das operações no modo append `a` utilizando o gerenciador de contexto `with`
    with open(filepath, "a") as file_:
    
        # Escrevendo a operação no arquivo, referenciado pelo nome `file_`, juntamente do timestamp e user
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result} \n")

# Captura um erro de permissão, imprimindo sua mensagem e encerrando o programa.
# Nesse caso, o erro é estourado caso o programa tente abrir um arquivo num diretório 
# onde o usuário não tenha permissão de acesso.
except PermissionError as e:

    # Log do tipo error, com a mensagem capturada da exceção PermissionError.
    log.error(str(e))
    sys.exit(1)

# Outra maneira de escrever a log da operação no arquivo usando a função `print()`
#print(f"{operation}, {n1}, {n2} = {result} \n", file=open(filepath, "a"))

# Imprime o resultado na tela.
print(f"O resultado é {result}")