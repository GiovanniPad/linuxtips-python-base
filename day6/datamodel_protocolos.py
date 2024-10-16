#!/usr/bin/env python3

# Protocolos / Data Model

# Protocolo Printable - __str__ / __repr__

# Classe para representar uma cor
class Cor:  # Base Class
    icon = "⬜"
    english_name = "color"

    # Método que implementa o Protocolo Printable que define como
    # os objetos instanciados a partir dessa classe são exibidos
    # ao ser impressos, incluindo suas subclasses
    def __str__(self):
        return f"{self.icon}"

    # Método que implementa o protocolo Addible, que permite que os
    # objetos instaciados a partir dessa classe possam ser somados
    # a partir da lógica definida internamente nesse método
    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta)
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    icon = "🟨"
    english_name = "yellow"


class Azul(Cor):
    icon = "🟦"
    english_name = "blue"

    # Método que implementa o protocolo Sized, permitindo que
    # o tamanho dos objetos instanciados dessa classe seja mensurado
    def __len__(self):
        return 3


class Vermelho(Cor):
    icon = "🟥"
    english_name = "red"

    # Método que implementa o protocolo Sized, permitindo que
    # o tamanho dos objetos instanciados dessa classe seja mensurado
    def __len__(self):
        return 1


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"

    # Método que implementa o protocolo Sized, permitindo que
    # o tamanho dos objetos instanciados dessa classe seja mensurado
    def __len__(self):
        return 2


class Violeta(Cor):
    icon = "🟪"


print("Cores primárias")
print(Amarelo())
print(Azul())
print(Vermelho())

# Protocolo Addible

print(1 .__add__(2))  # = 1 + 2
print("Bruno" + "Rocha")
print([1, 2, 3] + [4, 5, 6])

amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print("Cores secundárias")
print("Amarelo + Vermelho", amarelo + vermelho)
print("Azul + Amarelo", azul + amarelo)
print("Vermelho + Azul", vermelho + azul)

# Protocolo Iterable


class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    # Método que implementa o protocolo Iterable, permitindo
    # que o objeto instanciado seja iterável a partir de loop ou então
    # consumido por um iterador
    def __iter__(self):
        return iter([cor for cor in self._cores])

    # Método que implementa o protocolo Container, permitindo
    # que seja possível verificador se um valor ou item está dentro
    # do objeto instanciado
    def __contains__(self, item):
        return item in [cor.icon for cor in self._cores]

    # Método que implementa o protocolo Sized, permitindo que
    # o tamanho dos objetos instanciados dessa classe seja mensurado
    def __len__(self):
        return len(self._cores)

    # Método que implementa o protocolo Subscritable, que permite
    # que com que o objeto instanciado dessa classe tenha disponível
    # o comportamento de realizar consultas de valores de dentro dele
    def __getitem__(self, item):
        # Verifica se a consulta é por meio de um índice ou slice
        if isinstance(item, (int, slice)):  # 0, 2:4
            return self._cores[item]
        # Verifica se a consulta é através do nome do item
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())
# print([str(cor) for cor in rgb._cores])

for cor in rgb:
    print(cor)

# Protocolo Container

print("🟩" in rgb)
print("🟪" in rgb)

# Protocolo Sized

nome = "Giovanni"
print(len(nome))

print(len(rgb))

# Protocolo Subscriptable

print(rgb[0])
print(rgb["azul"])
