from tkinter import Tk, Label, Entry, Button, StringVar

# Cria um janela principal
janela = Tk()

# Cria os componentes com suas características
label = Label(janela, text="Nome:")
nome = Entry(janela)
var = StringVar()
mensagem = Label(janela, textvariable=var)


# Função de callback ao apertar o botão `diga_ola`
def callback_say_hello():
    # Coleta o valor do campo
    nome_digitado = nome.get()
    # Atribui o valor a um campo
    var.set(f"Olá {nome_digitado} boas vindas!!!")


# Cria os botões para realizar as ações
diga_ola = Button(janela, text="Diga Olá", command=callback_say_hello)
sair = Button(janela, text="Sair", command=janela.destroy)

# Posiciona no próximo espaço disponível com `pack`
# `grid` é uma forma mais dinâmica de inserir elementos na tela
# usando do grid de linhas e colunas
label.grid(column=1, row=1)
nome.grid(column=2, row=1)
mensagem.grid(column=2, row=2)
diga_ola.grid(column=2, row=3)
sair.grid(column=2, row=4)

# Invoca o mainloop para exibir a janela
janela.mainloop()
