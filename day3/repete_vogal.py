#!/usr/bin/env python3
"""Repete vogais.

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma
das palavras com suas vogais duplicadas.

ex:
python3 repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Solução do professor

# Variável para armazenar as palavras processadas
words = []

# Loop infinito, encerra com ação do usuário
while True:

    # Pergunta a palavra ao usuário
    word = input("Digite uma palavra (ou enter para sair): ").strip()

    # Condição de parada, pressionar enter
    if not word:
        break

    
    final_word = ""
    # Para cada letra na palavra, se for uma vogal, duplicar e armazenar na nova variável,
    # senão, apenas armazenar a letra na nova variável.
    for letter in word:
        # TODO: Remover acentuação usando função

        # Verifica se a letra está dentro da string de letras "aeiou".
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter

        # If ternário, igual o if acima
        #final_word += letter * 2 if letter.lower() in "aeiou" else letter

    # Armazenar a letra processada na lista de palavras
    words.append(final_word)

# Imprime as palavras da lista `words`.
# Desempacota a lista, e cada valor (palavra) é separadado por uma quebra de linha.
print(*words, sep="\n")