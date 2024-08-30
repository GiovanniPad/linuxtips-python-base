import argparse

# Função para carregar dados.
# Chamada ao ser passada para o argumento `subcommand` o valor "load".
def load(filepath):
    """Loads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found {e}")

# Principal função do programa.
def main():
    # Definindo um objeto do tipo `parser` para coletar os argumentos CLI.
    parser = argparse.ArgumentParser(
        # Descrição do projeto.
        description="Dunder Mifflin Rewards CLI",
        # Mensagem enviada para o terminal.
        epilog="Enjoy and use with cautious.",
    )

    # Definindo o primeiro argumento da CLI.
    # `subcommand` é o nome do argumento,
    # `type` é o tipo de objeto do argumento,
    # `help` mensagem de ajuda referente ao argumento,
    # `choices` são os possíveis valores para o argumento,
    # `default` valor padrão, caso nenhum valor seja passado.
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help"
    )

    # Definindo o segundo argumento da CLI, mesma lógica do anterior.
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None
    )

    # Coleta os argumentos do objeto `parser`.
    args = parser.parse_args()

    # Invoca a função específica para cada valor de argumento passado.
    # Executa a função através da função `globals()`.
    globals()[args.subcommand](args.filepath)

    
# Ao invocar o programa através do comando `python3 -m dundie` e o 
# principal entry point do programa seja uma função, ela não vai ser chamada,
# para que ela seja chamada deve-se verificar se o atributo `__name__` possui o valor `__main__`, 
# já que ao executar o programa usando o comando `-m` do Python, 
# seu atributo `__name__` vai ter o valor de `__main__`.
if __name__ == "__main__":
    main()