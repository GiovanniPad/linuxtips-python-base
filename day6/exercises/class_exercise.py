#!/usr/bin/env python3
"""
Este programa pergunta ao usuário quais items ele deseja comprar
e calcula o valor total da compra.
"""
# Objeto para representar valores monetários
from decimal import Decimal


# Classe que representa um produto
class Product:
    """Represents a product"""
    def __init__(self, name, value):
        self.name = name
        self.value = Decimal(value)


# Classe que representa uma compra ou um carrinho
class Purchase:
    """Represents a client purchase"""
    def __init__(self, client_name, items=[]):
        self.client_name = client_name
        self.items = items

    def add_product_to_items(self, product_code, quantity):
        self.items.append([product_code, quantity])

    def calculate_total(self):
        total = 0
        for product_code, quantity in self.items:
            total += (products.get(product_code).value) * quantity
        return Decimal(total)


# Dicionário contendo o id dos produtos, cada um com sua instância
products = {
    1: Product("Maçã", 4.5),
    2: Product("Melância", 6.3)
}

# Listando os produtos para o cliente
print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for product_code, product_info in products.items():
    print(
        f"{product_code} -> {product_info.name} - R$ {product_info.value:.2f}"
    )

# Coletando o nome do cliente
client_name = input("Qual o seu nome: ").strip()

# Instanciando uma nova compra
purchase = Purchase(client_name)

# Loop para perguntar os produtos que o cliente deseja adicionar ao carrinho
while True:
    try:
        # Perguntando o código do produto para o cliente
        product_code_input = int(input("Código do produto: [enter para sair]"))
    # Caso digitar enter ele sai do loop
    except (ValueError):
        print("Saindo...")
        break

    # Verificando se o produto está cadastrado na lista de produtos
    if int(product_code_input) not in products:
        print("Codigo inválido, tente novamente.")
        continue

    # Perguntando a quantas unidades do produto o cliente deseja
    quantity = int(input("Quantas Unidades:").strip())
    # Verifica se a quantidade é menor ou igual a 0, sendo uma quantia inválida
    if quantity <= 0:
        print("Quantidade inválida, tente novamente.")
        continue

    # Adicionando o produto para o carrinho de items da compra
    purchase.add_product_to_items(int(product_code_input), quantity)


# Imprimindo o nome do cliente, quantos produtos ele tem no carrinho
# e o valor total da compra, executa assim que ele apertar <enter>
print(f"Olá, {purchase.client_name}")
print(f"No seu carrinho de compras tem {len(purchase.items)} item.")
print(f"O total da compra é {purchase.calculate_total():.2f}")
