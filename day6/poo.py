# componentes - P.O.O

# Classe `class` - MaterialDeEscritorio, Eletronico, Gadget, Fruta
# Objetos - Instâncias criadas a partir da classe - Caneta, Relogio, Banana
# Atributos - Valores definidos nas classes e nos objetos (instância)
# Método - Função definida no escopo da classe

# Declarando uma classe com o nome `Pessoa`
class Person:
    """Represents a person"""

    # Declarando os atributos da classe, são comuns para todas
    # as instâncias dessa classe
    company_name = "Dunder Mifflin"
    work_address = "Rua Stanton, Pensilvania"
    balance = 0

    # Data Model - Métodos dunder ou métodos mágicos
    # O método `__init__` é um método que é invocado no momento em que
    # a classe é instanciada. Os parâmetros passados dentro desse método
    # são únicos para a instância em questão, mesmo sendo mutáveis.
    # O primeiro argumento `self` é passado por meio de injeção de dependência
    # e representa a própria instância.
    def __init__(self, name, role="Undefined", prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # Declarando o método `add_points` que adiciona pontos para uma
    # instância, todas as instâncias dessa classe possuem esse método
    def add_points(self, value):
        if self.role == "Manager":
            value *= 2

        self.balance += value


# Instanciando a classe `Pessoa` em um objeto de nome `jim`,
# passando juntamente os seus argumentos individuais (argumentos de instância)
jim = Person(name="Jim Halpert", role="Salesman", prefered_colors=["Blue"])

# Executando o método para adicionar pontos para a instância `jim`
jim.add_points(100)

# Imprimindo o identificador (id) da instância `jim`,
# cada instância tem um id diferente, ou seja,
# são instâncias diferentes mesmo que sejam da mesma classe
# print(id(jim))

# Imprimindo os atributo da instância `jim`
print(jim.company_name, jim.name, jim.balance, jim.role, jim.prefered_colors)

# Toda classe por baixo dos panos é uma implementação de um dicionário,
# esse método dunder mostra isso, nesse caso mostra a implementação da classe
# print(Person.__dict__)
# Mesma situação acima, porém aqui mostra a implementação e as informações
# da instância `jim` e não da classe `Person`
# print(jim.__dict__)

# Instanciando a classe `Person` passando os argumentos de instância e
# então adicionando 100 pontos para a instância `pam` e por fim,
# imprimindo os atributos da instância `pam`
pam = Person(name="Pam Besly", role="Receptionist")
pam.add_points(100)
print(pam.company_name, pam.name, pam.balance, pam.role, pam.prefered_colors)
