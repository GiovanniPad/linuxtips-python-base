# Biblioteca que interage com o SO
import os
# Biblioteca para randomizar coisas
import random
# Prompt igual ao `input` mas do rich, permite personalizar
from rich.prompt import Prompt
# Console do rich, permite personalizar
from rich.console import Console


# Estilo da letra correta
def posicao_correta(letra):
    return f"[black on green]{letra}[/]"


# Estilo da letra na posição errada
def posicao_incorreta(letra):
    return f"[black on yellow]{letra}[/]"


# Estilo da letra errada
def letra_errada(letra):
    return f"[black on white]{letra}[/]"


# Constantes
DIR = os.path.abspath(os.path.dirname(__file__))
MENSAGEM = (
    f"{posicao_correta("Boas vindas ")}"
    f"{posicao_incorreta("ao ")}"
    f"{letra_errada("Pylavras!")}"
)
INSTRUCAO = "Adivinha a palavras de 5 letras.\n"

# Escolhe uma palavra aleatória do arquivo
palavra_correta = random.choice(
    open(os.path.join(DIR, "assets", "palavras.txt")).readlines()
).strip().upper()

# Variáveis de controle
tentativas = 6
rodadas = 0

# Mensagens para o usuário
console = Console()
console.print(MENSAGEM)
console.print(INSTRUCAO)
# console.print(palavra_correta)


# Define os acertos e erros do usuário ao adivinhar a palavra
def computa_tentativa(tentativa):
    acertos = []
    for i, letra in enumerate(tentativa):
        if tentativa[i] == palavra_correta[i]:
            acertos.append(posicao_correta(letra))
        elif letra in palavra_correta:
            acertos.append(posicao_incorreta(letra))
        else:
            acertos.append(letra_errada(letra))
    return "".join(acertos)


# loop principal
acertados = []
while rodadas < tentativas:
    # Coleta a palavra do usuário
    tentativa = Prompt.ask("Digite [green]5[/] letras").strip().upper()
    # Valida a palavra
    if len(tentativa) != 5:
        console.print("Erro: Digite exatamente [red]5[/] letras.")
        continue
    rodadas += 1

    # Verifica os acertos e erros
    acertos = computa_tentativa(tentativa)
    acertados.append(acertos)

    # Limpa o console
    console.clear()

    # Imprime os acertos e erros
    for acerto in acertados:
        console.print(acerto)

    # Finaliza ao acertar
    if tentativa == palavra_correta:
        break

console.print(f"Pylavras: {rodadas}/{tentativas}")
