# setuptools
from setuptools import setup, find_packages


setup(
    # Nome do executável, instalador do projeto
    name="dundie",
    # Versão do projeto, segue o padrão Semantic Versioning
    version="0.1.0",
    # Descrição do projeto
    description="Reward point system for Dunder Mifflin",
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
    }
)