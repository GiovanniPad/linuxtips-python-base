#!/usr/bin/env python3

names = ["Bruno", "João", "Bernardo", "Barbara", "Brian"]

# TODO: Usar lambdas

def starts_with_b(text):
    return text[0].lower() == "b"

print(*list(filter(starts_with_b, names)))