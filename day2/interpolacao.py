#!/usr/bin/env python3

email_tmpl = """
    Olá, %(nome)s
    Tem interesse em comprar %(produto)s?
    Este produto é ótimo para resolver

    %(texto)s

    Clique agora em %(link)s
    
    Apenas %(quantidade)d disponíveis!
    
    Preço promocional %(preco).2f
"""

clientes = ["Giovanni", "Beatriz", "Zeca"]

for cliente in clientes:
    print(
        email_tmpl 
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escreve muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 5,
            "preco": 50.5,
        }
    )