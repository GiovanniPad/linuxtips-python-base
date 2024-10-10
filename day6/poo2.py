# Frutaria

# Classe `Fruit` que representa uma fruta.
class Fruit:
    """Represent a fruit."""
    # Método especial `__init__` inicializador da instância
    # definindo os atributos de instâncias (individuais)
    def __init__(self, name, color):
        self.name = name
        self.color = color


# Instanciando a classe em um objeto `apple`
apple = Fruit("Apple", "red")
print(apple.name, apple.color)

# Instanciando a classe em um objeto `banana`
banana = Fruit("Banana", "yellow")
print(banana.name, banana.color)
