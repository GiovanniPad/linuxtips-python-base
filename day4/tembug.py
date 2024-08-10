#!/usr/bin/env python3

def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for letter in word:
        if letter.lower() in "aeiouãõâôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
    return final_word


# Debbuging com prints
# def repete_vogal_print(word):
#     """Retorna a palavra com as vogais repetidas."""
#     final_word = ""
#     for index, letter in enumerate(word):
#         # usamos enumerate para ajudar a sabermos as voltas do loop
#         print(f"{index=} {letter=}") # `variable=` existe a partir do python 3.7>
#         if letter.lower() in "aeiouãõâôêéáíó":
#             final_word = letter * 2
#         else:
#             final_word = letter
        
#         print(f"{final_word=}")
#     return final_word


#import pdb; pdb.set_trace() ou breakpoint()

print(repete_vogal("banana"))
