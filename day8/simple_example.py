import PySimpleGUI as sg

# Define um tema para o app
sg.theme("Material1")


# Função para realizar uma soma
def soma(x: int, y: int) -> int:
    return x + y


# Define o layout da janela, adicionando os widgets
# Cada lista é uma linha e cada elemento de cada lista representa
# uma coluna daquela linha
layout = [
    [sg.Text("Número x"), sg.Input(key="x", enable_events=True, size=(5, 1))],
    [sg.Text("Número y"), sg.Input(key="y", enable_events=True, size=(5, 1))],
    [sg.Text("", key="result")],
    [sg.Button("Calcular")],
    [],
    [sg.Button("Sair")]
]

# Cria a janela principal
window = sg.Window(title="Calculadora", layout=layout, margins=(100, 50))

# Loop para exibir a janela
while True:
    # Coleta os eventos e valores da janela o tempo todo
    event, values = window.read()

    # Define o evento para fechar a janela
    if event in (sg.WIN_CLOSED, "Sair"):
        break

    # Define o evento de calcular algo
    if event == "Calcular":
        # Coleta os valores dos widgets `x` e `y` (keys)
        x = int(values["x"].strip())
        y = int(values["y"].strip())

        # Calcula o resultado
        result = soma(x, y)
        # Adiciona o resultado ao widget `result` da janela
        window["result"].update(result)

# Fecha e destrói a janela
window.close()
