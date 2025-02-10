#!/usr/bin/env python3

# Biblioteca para criar Type Annotations
from typing import Optional, List

# Biblioteca de abstração do SQL Alchemy
# Funções e classes usadas para trabalhar com banco de dados
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Session,
    select,
    Relationship
)

# Biblioteca utilizada trabalhar com caminhos em SOs
from pathlib import Path

# Implementação um patch de correção
# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
# from sqlmodel.sql.expression import Select, SelectOfScalar
# SelectOfScalar.inherit_cache = True  # type: ignore
# Select.inherit_cache = True  # type: ignore


# Tabela criada para representar a relação N:N entre `Person` e `Dept`
# Essas tabelas são utilizadas para apoio e são chamadas de Link Table
# `SQLModel` representa a classe base da `SQLModel`
# `table=True` indica que o próprio nome da classe vai ser o nome da tabela
# no banco de dados
class PersonDeptLink(SQLModel, table=True):
    # Cria um atributo opcional do tipo Integer com `Optional[int]`
    # Específica que o valor padrão desse atributo é None, e ele é um campo
    # de chave primária e recebe uma chave estrangeira de `dept.id`, esses
    # constrains são aplicados utilizando `Field()`
    dept_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="dept.id"
    )
    # Cria um atributo opcional do tipo Integer com `Optional[int]`
    # Específica que o valor padrão desse atributo é None, e ele é um campo
    # de chave primária e recebe uma chave estrangeira de `person.id`, esses
    # constrains são aplicados utilizando `Field()`
    person_id: Optional[int] = Field(
        default=None, primary_key=True, foreign_key="person.id"
    )


# Classe que representa a entidade `Person` no banco de dados
# `SQLModel` representa a classe base da `SQLModel`
# `table=True` indica que o próprio nome da classe vai ser o nome da tabela
# no banco de dados
class Person(SQLModel, table=True):
    # Cria um atributo opcional do tipo Integer com `Optional[int]`
    # Específica que o valor padrão desse atributo é None, e ele é um campo
    # de chave primária, esses constrains são aplicados utilizando `Field()`
    id: Optional[int] = Field(default=None, primary_key=True)
    # Atributo com o nome `name` do tipo str (string)
    name: str

    # Atributo para representar o relacionamento virtual entre Person e Balance
    # `back_populates` indica que uma instância de Person vai ser populada ao
    # criar uma instância de Balance, isso faz com que as instâncias sejam
    # atualizadas quando houver uma alteração em alguma delas
    balance: "Balance" = Relationship(back_populates="person")

    # Atributo para representar o relacionamento virtual N:N, é um atributo do
    # tipo lista com instâncias de Dept dentro dela
    # `back_populates` popula automaticamente depts quando uma instância de
    # Person foi criada, isso faz com que as instâncias sejam atualizadas
    # quando houver uma alteração em alguma delas
    # `link_model` indica qual a Table Link de apoio a ser usada
    depts: List["Dept"] = Relationship(
        back_populates="people", link_model=PersonDeptLink
    )


# Classe que representa a entidade `Balance` no banco de dados
# `SQLModel` representa a classe base da `SQLModel`
# `table=True` indica que o próprio nome da classe vai ser o nome da tabela
# no banco de dados
class Balance(SQLModel, table=True):
    # Cria um atributo opcional do tipo Integer com `Optional[int]`
    # Específica que o valor padrão desse atributo é None, e ele é um campo
    # de chave primária, esses constrains são aplicados utilizando `Field()`
    id: Optional[int] = Field(default=None, primary_key=True)
    # Atributo de nome `value` do tipo int
    value: int

    # Atributo para representar a chave estrangeira no banco de dados
    # É um atributo do tipo int e a chave estrangeira é definida através
    # de `Field()` e `foreign_key` indica o campo da tabela Person que irá
    # fornecer a chave estrangeira
    person_id: int = Field(foreign_key="person.id")

    # Cria um atributo de relacionamento virtual entre o atributo `balance` de
    # Person, faz com que as alterações sejam refletidas em ambos, caso houver
    # O atributo é definido como uma instância de Person
    person: Person = Relationship(back_populates="balance")


# Classe que representa a entidade `Dept` no banco de dados
# `SQLModel` representa a classe base da `SQLModel`
# `table=True` indica que o próprio nome da classe vai ser o nome da tabela
# no banco de dados
class Dept(SQLModel, table=True):
    # Cria um atributo opcional do tipo Integer com `Optional[int]`
    # Específica que o valor padrão desse atributo é None, e ele é um campo
    # de chave primária, esses constrains são aplicados utilizando `Field()`
    id: Optional[int] = Field(default=None, primary_key=True)
    # Atributo com o nome `name` do tipo string
    name: str

    # Atributo que contém um relacionamento virtual e é do tipo `List` com
    # instâncias de Person
    # `back_populates` popula automaticamente people quando uma instância de
    # Dept foi criada, isso faz com que as instâncias sejam atualizadas
    # quando houver uma alteração em alguma delas
    # `link_model` indica qual a Table Link de apoio a ser usada
    people: List["Person"] = Relationship(
        back_populates="depts", link_model=PersonDeptLink
    )


# Cria o caminho para o arquivo do banco de dados
database_path = Path(".", "day7", "archives", "sqlmodel.db")
# Define uma conexão com o banco de dados, criando uma `engine`, especificando
# o tipo do banco e sua string de conexão
# `echo=False` faz com a cada query os comandos
# não sejam exibidos automaticamente
engine = create_engine("sqlite:///" + str(database_path), echo=False)
# Cria todas as tabelas no banco de dados com base nas classes criadas
# `bind` indica qual a engine a ser usada
SQLModel.metadata.create_all(bind=engine)

# Cria uma sessão `Session` para ler e manipular dados do banco
# A sessão é criada com base em uma conexão `engine`
# É usado um gerenciador de contexto para fechar a conexão automaticamente
with Session(engine) as session:
    # Cria duas pessoas (instancia) e adiciona elas a sessão
    # para que sejam adicionadas no banco, por fim confirma as alterações
    # person = Person(name="Bruno")
    # session.add(person)
    # person = Person(name="Guido")
    # session.add(person)
    # session.commit()

    # Cria uma query para retornar todos os registros da tabela Person `select`
    # Executa a query com `exec` coletando os resultados
    # Itera sobre cada registro e adiciona um Balance para cada registro
    # criando o relacionamento
    # Por fim, adiciona os comandos a sessão é confirma as alterações
    # sql = select(Person)
    # results = session.exec(sql)
    # for person in results:
    #     balance = Balance(value=60, person=person)
    #     session.add(balance)
    # session.commit()

    # Primeira forma de realizar consulta JOIN,
    # utilizando os relacionamentos virtuais
    # sql = select(Person)
    # results = session.exec(sql)
    # for person in results:
    #     print(person.name, person.balance.value)

    # Segunda forma de realizar consulta JOIN com filtro `where`
    # também utiliza os relacionamentos virtuais
    # sql = select(Balance).where(Balance.value > 3)
    # results = session.exec(sql)
    # for balance in results:
    #     print(balance.person.name, balance.value)

    # Terceira forma de realizar consulta JOIN, utilizando ambas as tabelas
    # na query e usando um filtro `where` para relacionar ambas corretamente
    # Por fim, executa o comando e itera (desempacotando) sobre cada instância
    # do relacionamento
    # sql = select(Person, Balance).where(Balance.person_id == Person.id)
    # results = session.exec(sql)
    # for person, balance in results:
    #     print(person.name, balance.value)

    # Quarta forma de realizar consulta JOIN, utilizando ambas as tabelas
    # na query e usando a função `join` indica a tabela alvo e o tipo do JOIN
    # que é um LEFT OUTER JOIN
    # Executa e itera sobre cada registro
    # (desempacotando, pois retorna uma tupla)
    # sql = select(Person, Balance).join(Balance, isouter=True)
    # results = session.exec(sql)
    # for person, balance in results:
    #     print(person.name, balance.value)

    # Adiciona os departamentos a tabela Dept
    # for name in ["Sales", "Engineering", "Quality"]:
    #     session.add(Dept(name=name))

    # session.commit()

    # Coleta o nome do departamento "Sales" e pega apenas o primeiro resultado
    # sales = session.exec(select(Dept).where(Dept.name == "Sales")).first()
    # Também coleta o nome do departmento "Quality" e apenas o primeiro
    # resultado
    # quality = session.exec(
    #     select(Dept).where(Dept.name == "Quality")
    # ).first()

    # Cria um novo registro de uma Person,
    # especificando o nome, o saldo e os departamentos
    # person = Person(
    #     name="Jim",
    #     balance=Balance(value=100),
    #     depts=[sales, quality]
    # )
    # Adiciona o novo registro na sessão
    # session.add(person)
    # Confirma as alterações
    # session.commit()

    # Retorna e imprime os departamentos do funcionário que tem o nome "Jim"
    person = session.exec(select(Person).where(Person.name == "Jim")).first()
    print(f"Departments of {person.name}", person.depts, sep="\n")

    # Retorna e imprime todas as pessoas no departamento de "Sales"
    sales = session.exec(select(Dept).where(Dept.name == "Sales")).first()
    print(f"People on {sales.name}", sales.people, sep="\n")
