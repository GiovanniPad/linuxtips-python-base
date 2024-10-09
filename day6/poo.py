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

    # Declarando o método `add_points` que adiciona pontos para uma
    # instância, todas as instâncias dessa classe possuem esse método
    def add_points(person, value):
        if person.role == "Manager":
            value *= 2

        person.balance += value


# Instanciando a classe `Pessoa` em um objeto de nome `jim`
jim = Person()
# Definindo os atributos de instância, seus valores seram únicos
# somente para essa instância
jim.name = "Jim Halpert"
jim.role = "Salesman"

# Executando o método para adicionar pontos para a instância `jim`
jim.add_points(100)

# Imprimindo o identificador (id) da instância `jim`, cada uma tem um id
# diferente, ou seja, são instâncias diferentes,
# mesmo que sejam da mesma classe
print(id(jim))

# Imprimindo os atributo de classe e de instância
print(jim.company_name)
print(jim.name)
print(jim.balance)

# Toda classe por baixo dos panos é uma implementação de um dicionário,
# esse método dunder mostra isso, nesse caso mostra a implementação da classe
print(Person.__dict__)
# Mesma situação acima, porém aqui mostra a implementação e as informações
# da instância `jim` e não da classe `Person`
print(jim.__dict__)
