import os

# setuptools
from setuptools import setup, find_packages

# Função para ler e retornar o conteúdo de arquivos.
def read(*paths):
    """Read the contents of a text fil safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    # Retorna o caminho para pasta em que o arquivo que executa essa linha está.
    # `__file__` indica o nome do arquivo em questão.
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()
    
# Função para retornar as dependências dos arquivos de requirements.
def read_requirements(path):
    """Return a list of requirements from a text file."""
    # Retorna uma lista com as dependências usando list comprehension.
    return [
        line.strip()
        for line in read(path).split("\n")
        # Não insere linhas que não sejam apenas de dependências.
        if not line.startswith(("#", "git+", '"', "-"))
    ]

    
setup(
    # Nome do executável, instalador do projeto
    name="dundie",
    # Versão do projeto, segue o padrão Semantic Versioning
    version="0.1.0",
    # Descrição do projeto
    description="Reward point system for Dunder Mifflin",
    # Descrição completa do projeto, funciona como uma "documentação".
    long_description=read("README.md"),
    # Tipo do arquivo de conteúdo da descrição completa.
    long_description_content_type="text/markdown",
    # Autor do programa
    author="Giovanni Padilha",
    # Busca todos os pacotes que tem `__init__.py` no diretório
    packages=find_packages(),
    # Dicionário de entry points, onde a chave é o tipo do entry point e o valor são os caminhos para os entry points.
    # Adicinando uma função `main()` do arquivo `__main__.py` como entry point de linha de console.
    entry_points={
        "console_scripts": [
            "dundie = dundie:__main__.main"
        ]
    },
    # Dependências padrões, vão ser instaladas sempre.
    install_requires=read_requirements("requirements.txt"),
    # Dependências opcionais, instaladas de acordo com o uso.
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    }
) 