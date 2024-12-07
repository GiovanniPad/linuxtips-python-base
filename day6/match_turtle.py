#!/usr/bin/env python3

# Pattern Match Estrutural

# Biblioteca gráfica para criar um terminal próprio de desenho para estudos.
from turtle import Turtle

print(
    """\
    Jogo da Tartaruga

    Comandos:
        move x y
        move steps
        turn angle (default 90)
        draw shape size (line|circle)
        write text
        stop | exit
    """
)

# Instanciado a classe Turtle.
turtle = Turtle()
# Definindo o formato do ponteiro.
turtle.shape("turtle")
# Definindo a velocidade do ponteiro.
turtle.speed(3)
# Definindo a cor e o preenchimento do ponteiro.
turtle.color("blue", "yellow")
# Definindo a caneta de escrita/desenho para cima.
turtle.penup()

# Loop infinito para mostrar a interface gráfica.
while True:
    # Capturando os comandos do terminal turtle.
    # Indicando a variável como uma lista de strings.
    command: list[str] = input("turle > ").strip().split()
    # Estrutura match que verifica a estrutura alvo, nesse caso,
    # a variável `command`.
    # É como se fosse um `switch` de outras linguagens.
    match command:  # target

        # Verifica se uma lista com dois elementos e
        # o primeiro elemento é igual ao texto "move".
        case ["move", *points]:
            # Match para verificar a quantidade de pontos passados para mover.
            match points:
                # Verifica se é uma lista com dois elementos.
                case [x, y]:
                    # Move o ponteiro numa posição x e y,
                    # como um plano cartesiano.
                    turtle.goto(float(x), float(y))
                # Verifica se é uma lista com um elemento
                case [steps]:
                    turtle.forward(float(steps))

        # Verifica se uma lista com dois elementos e
        # o primeiro elemento é igual ao texto "turn".
        case ["turn", *options]:

            # Estrutura match para verificar a variável `options`
            match options:
                # Verifica se é uma lista com um elemento
                case [angle]:
                    # Gira o ponteiro para a direita em um ângulo específicado
                    turtle.right(float(angle))
                # Caso especial, caso nenhum case serviu, esse é executado
                case _:
                    # Gira o ponteiro em 90 graus para a direita
                    turtle.right(90)

        # Verifica se uma lista com três elementos e
        # o primeiro elemento é igual ao texto "draw".
        case ["draw", shape, size]:
            # Coloca a caneta do ponteiro para baixo, para desenhar
            turtle.pendown()
            # Match para verificar a variável shape da lista
            match shape:
                # Verifica se é para desenhar um círculo
                case "circle":
                    # Desenha um círculo a partir de um tamanho `size`
                    turtle.circle(float(size))
                # Verifica se é para desenhar uma linha
                case "line":
                    # Desenha uma linha de tamanho `size`
                    turtle.forward(float(size))
            # Coloca a caneta para cima
            turtle.penup()

        # Verifica se uma lista com dois elementos e
        # o primeiro elemento é igual ao texto "write".
        case ["write", *text]:
            # Desenha um texto de várias palavras, definindo um
            # alinhamento como `center` e fonte de tamanho `16pt 20`.
            turtle.write(" ".join(text), None, "center", "16pt 20")

        # Verifica se é uma lista de três elementos e se algum elemento
        # é "exit", "stop" ou "quit".
        case ["exit" | "stop" | "quit"]:
            # Fecha a aplicação.
            break

        # Caso especial, para caso se nenhum `case` for verdadeiro.S
        case _:
            print("Invalid command")
