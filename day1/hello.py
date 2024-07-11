#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável de ambiente LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI argument `--lang`

Ou o usuário terá que digitar.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
# Metadados com informações adicionais.
__version__ = "0.1.4"
__author__ = "Giovanni Padilha"
__license__ = "Unlicense"

# Biblioteca que interage com o Sistema Operacional.
import os
# Biblioteca que interage com o ambiente de execução do Python.
import sys
# Biblioca para a criação de logs.
import logging

# Criando um Logger e um Handler específicos para exibir mensagens de log.
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("hello.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Define um bloco principal de um script Python,
# apesar de estar caindo em desuso.
#if __name__ == "__main__":

# Dicionário declarando os argumentos que podem ser declarados na CLI.
arguments = {"lang": None, "count": 1}

# `sys.argv` da biblioteca `sys` coleta todos os argumentos passados na CLI e retorna uma lista.
# Iterando nessa lista de argumentos a partir da segunda posição.
for arg in sys.argv[1:]:

    # Bloco onde se espera um erro.
    try:
        # Divide a string de cada argumento em dois usando o caractere "=" para separar.
        # Desempacota em duas variáveis, o primeiro é a chave e o segundo o valor.
        key, value = arg.split("=")

    # Capturando uma exceção do tipo valor.
    # Exceção ocorre caso, ao passar o argumento CLI, o usuário usar um caractere diferente de `=`.
    except ValueError as e:

        # Exibindo um log do tipo error, com uma mensagem (atributo `message`) personalizada,
        # junto com o motivo do erro e a mensagem de erro gerada pela exceção.
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    # `lstrip("-")` remove os traços no início da string.
    # `strip()` remove os espaços em branco do início e do fim da string.
    key = key.lstrip("-").strip()
    value = value.strip()

    # Valida se o argumento (chave) está presente dentro do dicionário de argumentos válidos.
    if key not in arguments:

        # Mostra qual argumento é inválido.
        print(f"Invalid Option `{key}`")

        # `sys.exit()` encerra o script nessa linha.
        sys.exit()

    # Atribui o valor do argumento (chave) no dicionário.
    arguments[key] = value

# Coleta a língua passada no argumento para exibir a mensagem.
current_language = arguments["lang"]

# Verifica se nenhum argumento foi passado.
if current_language is None: 
    # TODO: Usar repetição

    # Verifica se a variável de ambiente `LANG` existe.
    # Se existir, usa ela como valor em vez do argumento da CLI.
    # Se não existir, pergunta pro usuário qual a língua que vai ser usada.
    if "LANG" in os.environ:
        # A função `getenv()` da biblioteca `os` coleta o valor de uma variável de ambiente.
        current_language = os.getenv("LANG")
    else:
        # `input()` pergunta algo ao usuário a partir da stdin.
        current_language = input("Choose language:")

# Fatia a língua atual, coletando apenas os últimos 5 caracteres.
current_language = current_language[:5]

# Dicionário, a chave é o país e o valor é a mensagem na língua do país em questão.
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

# Maneira de verificar implícita, não recomendada, pois não imprime nenhum erro.
# message = msg.get(current_language, msg["en_US"])

# Bloco onde se espera um erro.
try:
    message = msg[current_language]

# Captura um erro do tipo chave.
# Erro causado caso ao tentar acessar um dicionário, a chave passada não exista nele.
except KeyError as e:
    
    # Log do tipo error, contendo uma mensagem personalizada, juntamente com o valor errado passado,
    # e os valores que estão disponíveis e são suportados. 
    log.error(
        "Language is invalid, you passed %s, please choose from %s.",
        str(e),
        list(msg.keys())
    )
    sys.exit(1)

# A função `print()` imprime um conteúdo qualquer na tela (output).
# Ordem de Complexidade O(1) - Constante.
print(
    message * int(arguments["count"])
)