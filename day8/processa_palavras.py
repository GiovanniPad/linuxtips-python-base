"""Filtrar palavras que contém 5 letras
e remover os acentos
"""
import unicodedata


# tira acentos das palavras
def tira_acento(s):
    # Normaliza usando o "NFD"
    return unicodedata.normalize(
        "NFD", s
        # Codifica para ascii ignorando os caracteres que não são ascii
    ).encode(
        "ascii", "ignore"
        # Decodifica novamente para utf8 (já sem acentos)
    ).decode(
        "utf-8"
    )


# Abre o arquivo
original = open("assets/br-utf8.txt").readlines()

# Seleciona as palavras apenas com 5 letras
with open("assets/palavras.txt", "w") as palavras:
    palavras.write(
        "\n".join(
            tira_acento(p.strip().upper())
            for p in original
            if len(p.strip()) == 5
        )
    )
