#!/usr/bin/env python3
"""Repete vogais

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
__author__ = "Giovanni Padilha"

# Minha solução

# Variável contendo as vogais e variável para armazenar as palavras processadas
words = []
vowels = ["a", "e", "i", "o", "u"]

# Loop infinito, encerra com ação do usuário
while True:
    # Pergunta a palavra ao usuário
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    new_word = ""

    # Condição de parada, pressionar enter e então imprime todas as palavras processadas
    if not word:
        for word in words:
            print(word)
        break

    # Para cada letra na palavra, verificar se é uma vogal (sempre em minúsculo) e duplicá-la e adicionar a nova variável `new_word`.
    # Senão, apenas adicionar a letra sem duplicar na variável `new_word`.
    for letter in word:
        if letter.lower() in vowels:
            new_word += letter * 2
            continue
        new_word += letter

    # Atribui a palavra com as vogais duplicadas na lista de palavras.
    words.append(new_word)



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