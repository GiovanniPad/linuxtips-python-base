#!/usr/bin/env python3
"""Exemplos de uso de logs com a biblioteca logging do Python."""
__version__ = "0.1.0"
__license__ = "Unlicense"

# Biblioteca para interação com o SO.
import os
# Biblioteca para a geração de logs.
import logging

# Importando um módulo da biblioteca `logging` para modificar o Handler (aonde vai ser impresso a mensagem de log)
from logging import handlers

# Coletando uma variável de ambiente onde seu valor determina qual o nível de logs a serem exibidos.
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Código Boilerplate -> código repetitivo
# TODO: Mover para um módulo de utilidades
# TODO: usar lib (loguru)

# Criando a própria instância de um logger com o nome `logs.py` e atribuindo um level (nível) a ele,
# nesse caso, o nível vem a partir da variável `log_level` 
log = logging.Logger("logs.py", log_level)

# Cria um Handler, que vai determinar aonde essa log será exibida,
# no caso do `StreamHandler()` a mensagem vai ser exibida por padrão no strerr.
# Já no caso de `RotatingFileHandler()` a mensagem vai ser mandada para um arquivo de logs.
#ch = logging.StreamHandler()

# Determina qual o Level de log desse Handler, `ch` de Console Handler.
#ch.setLevel(log_level)

# Handler que interage com um arquivo
# - O primeiro parâmetro é o nome do arquivo de logs
# - O segundo parâmetro indica o tamanho de cada arquivo de log, recomendado `10**6` (1 Mb)
# - O terceiro parâmetro indica quantos arquivos vão ser criados, se for 0,
#   as novas mensagens de logs vão substituir as antigas quando o tamanho do arquivo exceder o definido,
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=500, # 10**6
    backupCount=10,
)
# Definindo o Level do FileRotatingHandler, `fh` de File Handler.
fh.setLevel(log_level)

# Definindo qual a formatação que a mensagem de log terá
# `asctime` é o dia e a hora do erro, `name` é o nome do Logger;
# `levelname` é o Level do erro, `lineno` indica a linha que ocorreu o erro;
# `filename` indica qual o arquivo que ocorreu, `message` é a mensagem do erro.
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)

# Atribui a formatação a um Handler.
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

# Adiciona o Handler personalizado a um Logger criado.
#log.addHandler(ch)
log.addHandler(fh)

# Levels de mensagens de erros disponíveis.
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro.")
log.error("Erro que afeta uma única execução.")
log.critical("Erro geral. ex: banco de dados sumiu")

# Exemplo de uso
try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))