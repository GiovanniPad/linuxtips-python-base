.PHONY: install virtualenv clean

# Comando para instalar as dependências para o ambiente de desenvolvimento.
install:
	@echo "Hello for dev enviroment"
	@.venv/bin/python3 -m pip install -e '.[dev]'

# Cria um ambiente virtual
virtualenv:
	@.venv/bin/python3 -m pip -m venv .venv

# Executa o ipython a partir do ambiente virtual
ipython:
	@.venv/bin/ipython

# Limpa arquivos não usados e de cache
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build