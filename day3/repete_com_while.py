#!/usr/bin/env python3

# Loop while, ocorre enquanto a condição de parada for Verdadeira (True)
n = 0
while n < 101: # loop infinito, main loop
    if n >= 40 and n <= 60:
        n += 1
        continue

    print(n)
    n += 1