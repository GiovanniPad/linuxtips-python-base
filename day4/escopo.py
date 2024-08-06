#!/usr/bin/env python3

# aqui começa o escopo global
nome = "Global"

def funcao():
    # aqui começa o escopo local da função
    nome = "Local"

    def funcao_interna(): # inner function / closure
        # aqui começa o escopo local da função interna
        #nome = "Interna"

        #print("Escopo local da função interna:", locals())
        #print("*" * 30)

        print(nome)
        return nome
        # aqui termina o escopo local da função interna

    #print("Escopo local da função:", locals())
    #print("=" * 30)

    funcao_interna()
    print(nome) # = print(locals()["nome"])

    return nome
    # aqui termina o escopo local da função

#print("Escopo global do programa:", globals())
#print("-" * 30)

funcao()
print(nome) # = print(globals()["nome"])
# aqui termina o escopo global