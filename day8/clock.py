"""
An App to show the current time.
"""

from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits


# Classe principal do app
class ClockApp(App):
    # Estilos aplicados a interface
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    # Junta os dígitos
    def compose(self) -> ComposeResult:
        yield Digits("")

    # Executa a função de atualizar o relógio e o timer
    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    # Atualiza o tempo do relógio
    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")


if __name__ == "__main__":
    app = ClockApp()
    app.run()
