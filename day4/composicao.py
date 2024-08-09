#!/usr/bin/env python3

# Lista com nomes.
names = ["Bruno", "João", "Bernardo", "Barbara", "Brian"]

# Estilo Funcional

# Estilo funcional, possui menos "side effects", pois cria menos objetos em memória.

print("Estilo Funcional")

# Usa uma função lambda dentro de uma função filter 
# para verificar se o nome começa com "b" ou não,
# os nomes já filtrados são então convertidos para uma lista e 
# desempacotados em um print com uma quebra de linha como separador.
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")

print()

# Estilo Procedural

# Realiza a mesma operação acima, a diferença é que segue um estilo procedural de programação.
print("Estilo Procedural")

# Função para retornar se o nome começa com "b" ou não.
def stars_with_b(text):
    """Return bool if text starts with b."""
    return text[0].lower() == "b"

# Usa a função filter para filtrar todos os nomes que começam com "b" na lista
# e depois converte o objeto filter para uma lista.
filtro = filter(stars_with_b, names)
filtro = list(filtro)

# Imprime cada nome na lista de nomes filtrados.
for name in filtro:
    print(name)