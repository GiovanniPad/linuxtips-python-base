# Biblioteca ORM para trabalhar com banco de dados relacionais
# `Column` define colunas nas tabelas
# `Integer` e `String` define o tipo de uma coluna
# `create_engine` cria uma conexão com o banco de dados
# `ForeignKey` define uma chave estrangeira
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
# `declarative_base` cria a classe base para criar outras classes modelos
# `sessionmaker` cria uma sessão para manipular e acessar dados no banco
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Bibliotecas para trabalhar com caminhos em SOs
from pathlib import Path

# Definindo o caminho local para o arquivo do banco de dados
database_path = Path(".", "day7", "archives", "database.db")
# Criando a classe base para criar as demais classes modelos
Base = declarative_base()


# Criando a classe `Person` que irá virar a tabela Person, herda de `Base`
class Person(Base):
    # Define o nome da tabela no banco de dados
    __tablename__ = "person"

    # Atributos que definem as colunas e seus tipos na tabela
    # Cria a coluna `id` com `Column` onde seu tipo de dado é `Integer`
    # `primary_key=True` significa que a coluna é uma chave primária
    # `index=True` indica que é uma coluna de índices
    # `autoincrement=True` indica que é uma coluna que tem o valor incrementado
    # automaticamente
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Cria uma coluna com o nome `name` que tem o tipo de dados `String`
    # com um limite de 255 caracteres, é um campo varchar
    name = Column(String(255))


# Cria a blasse `Balance` que irá virar a tabela Balance, herda de `Base`
class Balance(Base):
    # Define o nome da tabela no banco de dados
    __tablename__ = "balance"

    # Cria a coluna `id` com `Column` onde seu tipo de dado é `Integer`
    # `primary_key=True` significa que a coluna é uma chave primária
    # `index=True` indica que é uma coluna de índices
    # `autoincrement=True` indica que é uma coluna que tem o valor incrementado
    # automaticamente
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # Cria a coluna `value` com `Column` com o seu tipo de dado sendo `Integer`
    # `nullable=False` define que essa coluna é NOT NULL, não pode ser null
    value = Column(Integer, nullable=False)

    # Cria uma coluna `person_id` com `Column` com seu tipo sendo `Integer`
    # `ForeignKey(Person.id)` define que a coluna `person_id` é uma chave
    # estrangeira que vem da tabela `person` e da coluna `id`
    person_id = Column(Integer, ForeignKey(Person.id))

    # Define um relacionamento virtual usado apenas no Python para facilitar
    # `Person` indica de qual tabela vem a chave e `foreign_keys` indica
    # de qual atributo (coluna) vem a chave
    person = relationship("Person", foreign_keys="Balance.person_id")


# Cria uma conexão com o banco de dados, chamada de `engine`
# Nessa conexão é indicada o tipo do banco e o caminho/servidor e porta
engine = create_engine("sqlite:///" + str(database_path))

# Converte e cria todas as tabelas e colunas no banco de dados
# `bind` indica qual a conexão utilizada
Base.metadata.create_all(bind=engine)

# Cria uma classe de sessão utilizada para acessar e manipular dados
# do banco de dados, cria a instância com `sessionmaker`
# `autocommit=False` indica que os commits não vão ser feitos automaticamente
# `autoflush=False` indica que o histórico da sessão não vai ser apagado
# a cada commit
# `bind` indica qual a engine de conexão a ser usada
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Instância a classe da sessão para ser utilizada
session = SessionLocal()

# Cria uma instância de `Person`
# person = Person(name="Guido")
# Adiciona a instância a fila para ser inserida no banco
# session.add(person)

# Cria outra instância de `Person`
# person = Person(name="Beatriz")
# Adiciona a outra instância a fila para ser inserida no banco
# session.add(person)

# Confirma todas as instruções inseridas na sessão
# session.commit()

# Busca todos os registros da tabela `Person`
# results = session.query(Person)

# Itera sobre cada linha dos resultados
# for result in results:
#     # Cria uma instância de `Balance` e relaciona com cada registro
#     # de `Person`, por fim atribui um valor para cada instância de `Balance`
#     balance = Balance(value=40, person_id=result.id)
#     # Adiciona cada instância na sessão para ser inserida no banco
#     session.add(balance)

# Confirma todas as alterações no banco de dados
# session.commit()

# Realiza uma consulta entre duas tabelas, utilizando JOIN
# Em `query` é especificado quais colunas quer consultar
# `join` indica qual a tabela alvo e qual tipo de JOIN é usado,
# no caso LEFT JOIN
results = session.query(Person.name, Balance.value).join(Balance, isouter=True)

# Itera e imprime todas as linhas da consulta
for result in results:
    print(result)
