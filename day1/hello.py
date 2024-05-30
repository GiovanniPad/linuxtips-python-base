#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável de ambiente LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
# Metadados com informações adicionais.
__version__ = "0.0.1"
__author__ = "Giovanni Padilha"
__license__ = "Unlicense"

# Importando a biblioteca `os` que permite que o Python se comunique com o SO.
import os

# Define um bloco principal de um script Python,
# apesar de estar caindo em desuso.
#if __name__ == "__main__":

"""
A função `getenv()` da lib `os` coleta o valor de uma variável de ambiente.

- O primeiro parâmetro informa qual o nome da variável de ambiente.
- O segundo parâmetro informa um valor padrão, caso essa variável não existir.
"""
# O `[:5]` refere-se ao fatiamento da string, coletando apenas os 5 primeiros caracteres.
current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

"""
Estrutura condicional `if`, onde a expressão lógica será dada como true ou false,
e a partir desse valor booleano, é executado um bloco de código.

A palavra `elif` faz com que uma nova comparação possa ser adicionada na estrutura.
"""
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

# A função `print()` imprime um conteúdo qualquer na tela (output).
print(msg)