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
    packages=find_packages()
)