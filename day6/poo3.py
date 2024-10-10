# Classe `Triangle` que representa um triângulo
class Triangle:
    """Represents a triangle."""
    # Atributo de classe, igual para todas as instâncias
    side_qtd = 3

    # Método especial `__init__` (inicializador da classe)
    # definindo os atributos de instância (individuais)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Método para calcular a área,
    # os atributos são acessadas através do objeto `self`,
    # que representa a instância da classe
    def area(self):
        perimeter = self.a + self.b + self.c
        s = perimeter / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


# Instanciando um triângulo e imprimindo a sua área
triangle = Triangle(5, 6, 7)
print(triangle.area())

# Modificando o valor do lado `a` do triângulo e
# imprimindo o novo valor da área
triangle.a = 10
print(triangle.area())

# Lista contendo várias instâncias de triângulos
triangles = [
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(8, 15, 17),
    Triangle(12, 35, 37),
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(8, 15, 17),
    Triangle(12, 35, 37)
]
# Para cada triângulo na lista imprimir sua área
for triangle in triangles:
    print("A área do triângulo é:", triangle.area())
