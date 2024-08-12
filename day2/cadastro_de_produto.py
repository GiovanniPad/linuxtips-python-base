#!/usr/bin/env python3
"""Exemplo de uso de dicionários em Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Importa da biblioteca `pprint` a função pprint()
from pprint import pprint

# Criando um dicionário com os dados de um produto.
# A chave `cor` aponta para uma lista contendo as cores.
# A chave `dimensoes` aponta para um dicionário com chaves e valores, armazenando as dimensões.
produto = {
    "nome": "Caneta",
    "cores": ["Azul", "Branco"],
    "preco": 3.23,
    "dimensoes": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None
}

# Dicionário contendo os dados do cliente.
cliente = {
    "nome": "Giovanni"
} 

# Dicionário contendo os dados de uma compra.
# O cliente que comprou, o produto comprado e a quantidade.
# Os dados do cliente e do produto são passados via Dicionário.
compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
}

# Função de exibir na tela (output) de uma maneira melhor, mais estruturada.
#pprint(compra)

# Calcula o valor total da compra
total_compra = compra["produto"]["preco"] * compra["quantidade"]

# Usar várias chaves para acessar um valor, operação chamada de Traversing, acesso a um valor aninhado.
print(
    f"O cliente {compra['cliente']['nome']} "
    f"comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f"e pagou o total de {total_compra}"
    )
