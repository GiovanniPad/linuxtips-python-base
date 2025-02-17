# Imports
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.bubble import Button
from kivy.uix.textinput import TextInput


# Define uma classe principal para representar a janela,
# extende de `App`
class KivySum(App):
    # Função de build (construção) principal da janela
    # Nela que vai as configurações e widgets (componentes)
    def build(self):

        # Definindo o layout da janela
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Adiciona um widget de texto com as suas propriedades
        self.window.add_widget(
            Label(text="Calculator", font_size=40, color="#ffcc00")
        )

        # Widget para um input
        self.x = TextInput(
            multiline=False, padding_y=(2, 2), size_hint=(1, 0.5), font_size=30
        )
        # Adiciona o widget na janela
        self.window.add_widget(self.x)

        # Outro widget de input
        self.y = TextInput(
            multiline=False, padding_y=(2, 2), size_hint=(1, 0.5), font_size=30
        )
        # Adiciona o widget na janela
        self.window.add_widget(self.y)

        # Cria um campo vazio e adiciona ele a janela
        self.result = Label(text="", font_size=40, color="ffcc00")
        self.window.add_widget(self.result)

        # Widget de botão
        calcula = Button(
            text="Calcula",
            size_hint=(1, 0.5),
            bold=True,
            background_color="#00FFCE"
        )
        # Atribui ao botão uma ação `on_press` que executará uma funcão
        calcula.bind(on_press=self.calcula)
        # Adiciona o botão na janela
        self.window.add_widget(calcula)

        # Botão de sair
        sair = Button(
            text="Sair",
            size_hint=(0.5, 0.5)
        )
        # Adiciona o evento `on_press` para fechar a tela
        sair.bind(on_press=self.stop)
        # Adiciona o botão na janela
        self.window.add_widget(sair)

        # Retorna a janela com todos os widgets e configurações
        return self.window

    # Função para calcular uma soma
    def calcula(self, instance):
        self.result.text = str(int(self.x.text) + int(self.y.text))


# Executa a classe para exibir a janela (loop)
if __name__ == "__main__":
    KivySum().run()
