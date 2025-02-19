# Bibliotecas
import pygame as pg
import pygame.locals as keys
import os
import random

# Constantes de cores e tamanhos
DIR = os.path.abspath(os.path.dirname(__file__))
TAMANHO_JANELA = (800, 800)
VERDE = (60, 220, 0)
CINZA = (50, 50, 50)
AMARELO = (255, 240, 60)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Dimensões dos objetos na tela
largura, altura = TAMANHO_JANELA
largura_estrada = int(largura / 1.6)
largura_separador = int(largura / 200)
lado_direito = largura / 2 + largura_estrada / 4
lado_esquerdo = largura / 2 - largura_estrada / 4

# Configurações da janela principal
pg.init()
pg.display.set_caption("Catch a Beer")
tela = pg.display.set_mode(TAMANHO_JANELA)
tela.fill(VERDE)
pg.display.update()

# Fonte
letra = pg.font.SysFont("Comic Sans MS", 30)
letra_grande = pg.font.SysFont("Comic Sans MS", 90)

# Jogador
jogador = pg.image.load(os.path.join(DIR, "assets", "player", "player.png"))
jogador = pg.transform.scale(jogador, (150, 150))
posicao_jogador = jogador.get_rect()
posicao_jogador.center = lado_direito, altura * 0.8

# FPS
clock = pg.time.Clock()


# Gera cerveja aleatoria e retorna o objeto e a posição
def carrega_cerveja_aleatoria():
    i = random.randint(1, 5)
    cerveja = pg.image.load(os.path.join(DIR, "assets", "beers", f"{i}.png"))
    cerveja = pg.transform.scale(cerveja, (100, 100))
    posicao_cerveja = cerveja.get_rect()

    if random.randint(0, 1) == 0:
        posicao_cerveja.center = lado_direito, altura * 0.2
    else:
        posicao_cerveja.center = lado_esquerdo, altura * 0.2

    return cerveja, posicao_cerveja


# Carrega uma nova cerveja
cerveja, posicao_cerveja = carrega_cerveja_aleatoria()

# Variáveis de estado/controle
executando = True
velocidade = 1
bebeu = 0
perdeu = 0
rodadas = 0

# loop principal
while executando:
    # Determina o estado do jogo
    rodadas += 1
    clock.tick(144)
    posicao_cerveja[1] += velocidade
    if rodadas == 2000:
        velocidade += 0.15
        rodadas = 0
        print("Level Up", velocidade)

    # Detectando colisão
    if (
        10 < (posicao_jogador[1] - posicao_cerveja[1]) < 30
        and posicao_jogador[0] == posicao_cerveja[0] - 25
    ):
        bebeu += 1
        som = pg.mixer.music.load(
            os.path.join(DIR, "assets", "sound", "sensacional.mp3")
        )
        pg.mixer.music.play(0)
        cerveja, posicao_cerveja = carrega_cerveja_aleatoria()

    # captura os eventos
    for event in pg.event.get():
        if event.type == keys.QUIT:
            executando = False
        if event.type == keys.KEYDOWN:
            if event.key in (keys.K_a, keys.K_LEFT):
                posicao_jogador = posicao_jogador.move(
                    (-int(largura_estrada / 2), 0)
                )
            elif event.key in (keys.K_d, keys.K_RIGHT):
                posicao_jogador = posicao_jogador.move(
                    (int(largura_estrada / 2), 0)
                )

    # Desenhos necessários na tela
    # Estrada
    pg.draw.rect(
        tela,
        CINZA,
        (largura / 2 - largura_estrada / 2, 0, largura_estrada, altura)
    )

    # Separador
    pg.draw.rect(
        tela,
        AMARELO,
        (largura / 2 - largura_separador / 2, 0, largura_separador, altura)
    )

    # Bordas
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 - largura_estrada / 2 + largura_separador * 2,
            0,
            largura_separador,
            altura
        )
    )
    pg.draw.rect(
        tela,
        BRANCO,
        (
            largura / 2 + largura_estrada / 2 - largura_separador * 2,
            0,
            largura_separador,
            altura
        )
    )

    # Cria um título
    titulo = letra.render(
        f"Catch a Beer! bebeu: {bebeu} vacilou: {perdeu}", True, BRANCO
    )

    # Carrega os objetos na tela
    tela.blit(titulo, (largura / 5, 0))
    tela.blit(jogador, posicao_jogador)
    tela.blit(cerveja, posicao_cerveja)

    # Atualiza a tela
    pg.display.update()

    # Calcula o resultado final
    if posicao_cerveja[1] > altura:
        perdeu += 1
        cerveja, posicao_cerveja = carrega_cerveja_aleatoria()

    # Condição de parada do jogo
    if perdeu > 3:
        som = pg.mixer.music.load(
            os.path.join(DIR, "assets", "sound", "zika.mp3")
        )
        pg.mixer.music.play(0)
        msg = letra_grande.render("GAME OVER", True, AMARELO)
        tela.blit(msg, (largura / 4, 100))
        pg.display.update()
        wait_key = True
        while wait_key:
            for event in pg.event.get():
                if event.type == keys.KEYDOWN:
                    wait_key = False
        break

# Encerra o processo do jogo
pg.quit()
