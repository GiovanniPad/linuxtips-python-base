def main():
    print("Executing dundie from entry point.")

# Ao invocar o programa através do comando `python3 -m dundie` e o 
# principal entry point do programa seja uma função, ela não vai ser chamada,
# para que ela seja chamada deve-se verificar se o atributo `__name__` possui o valor `__main__`, 
# já que ao executar o programa usando o comando `-m` do Python, 
# seu atributo `__name__` vai ter o valor de `__main__`.
if __name__ == "__main__":
    main()