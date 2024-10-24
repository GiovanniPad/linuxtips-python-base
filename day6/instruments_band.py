#!/usr/bin/env python3

# Abstração e Herança com dataclasse?
# Tem enum no Python?
# Dataclasses com valor default dão erro
# Para que serve o super() ?

# Módulo `abc`, classe `ABC` e decorator `abstractmethod`
from abc import ABC, abstractmethod

# Módulo `dataclasses`, decorator `dataclass` e função `field`
from dataclasses import dataclass, field

# Módulo `enum`, classe `Enum`
from enum import Enum


# Enumeração / Enumerador
# Criando um enumerador que armazena uma lista de estados,
# para que seja possível comparar seus estados com strings é
# necessário herdar da classe `str` também
class InstrumentKind(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"


# Enumerador `Distortion`, mesmas características do acima
class Distortion(str, Enum):
    wave = "wave"
    whisper = "whisper"


# Classe abstrata que herda da classe `ABC` Abstract Base Class
class ABCInstrument(ABC):

    # Cria um método abstrato, tornando sua implementação obrigatória
    # em todas as classes derivadas
    @abstractmethod
    def play(self): ...


# Decorator que indica que é uma classe de dados,
# criando o `__init__` automaticamente
@dataclass
# Classe Mixin é uma classe que é usado para misturar e adicionar novos
# atributos/métodos a outras classes
# Nunca devem ser usadas sozinhas, devem sempre virem
# acompanhadas de outra classe
class DataInstrumentMixin:
    name: str
    sound: str
    kind: InstrumentKind
    # Maneira de inicializar um atributo default mutável dentro de uma classe
    # A função `field` adiciona um atributo a classe com o valor None,
    # depois o `default_factory` torna aquele atributo uma lista vazia
    colors: list = field(default_factory=list)


# Classe para representar um Instrumento,
# que herda da classe abstrata `ABCInstrument`
# e da classe Mixin `DataInstrumentMixin`
class Instrument(DataInstrumentMixin, ABCInstrument):
    ...


# Indica que é uma dataclass, criando o `__init__` automaticamente
@dataclass
# Classe que representa um violão, herdando de `Instrument`
class Guitar(Instrument):
    # Definindo atributos próprio dessa classe derivada
    n_strings: int = 6
    sound: str = "Ding Ding Ding"
    # Usando os valores do enum para atribuir o tipo do instrumento
    kind: InstrumentKind = InstrumentKind.string
    # Maneira de criar uma lista com valores padrão dentro de uma classe,
    # mesma lógica de criar uma lista vazia (anteriormente), porém passando uma
    # lambda que retorna a lista com os valores desejados
    colors: list = field(default_factory=lambda: ["red", "black"])

    # Implementado o método abstrato `play` da classe abstrata
    def play(self):
        return self.sound


# Indica que é uma dataclass, criando o `__init__` automaticamente
@dataclass
# Classe que representa uma guitarra, herdando de `Guitar`
class EletricGuitar(Guitar):
    # Definindo atributo próprio dessa classe derivada
    sound: str = "Wah Wah Wah"

    # Sobrescrevendo o retorno do método `play` da classe pai,
    # passando seu próprio parâmetro
    def play(self, distortion: Distortion = Distortion.wave):
        # Utilizando o `super` é possível coletar o método `play` da classe pai
        return_from_base_class = super().play()  # Method Resolution Order MRO

        # Lógica para definir o retorno, utilizando enums
        # É possível usar `is` com Enum pois ele é único na memória,
        # já que não deve ser instanciado
        # Melhor forma de comparar um enum é com ele mesmo
        if distortion is Distortion.wave:
            return "~~~".join(return_from_base_class.split())
        elif distortion is Distortion.whisper:
            return "...".join(return_from_base_class.split())
        return return_from_base_class


# Indica que é uma dataclass, criando o `__init__` automaticamente
@dataclass
# Classe que representa uma flauta, herdando de `instrument`
class Flute(Instrument):
    # Definindo atributos próprios dessa classe
    sound: str = "Flu Flu Flu"
    kind: InstrumentKind = InstrumentKind.wind
    # Definindo uma lista com valores padrões dentro de uma classe
    colors: list = field(default_factory=lambda: ["beige", "white"])

    # Implementando o método abstrato (obrigatório) da classe pai abstrata
    def play(self):
        return self.sound


# O MyPy vai acusar um erro, pois não se deve instanciar uma classe abstrata
# x = Instrument()

# Instanciando classes e testando suas implementações

gianini = Guitar("Giannini m2", kind=InstrumentKind.string)
print(gianini.play())
print(gianini.colors)

yamaha = Flute("Yamaha Magic Flute",
               kind=InstrumentKind.wind,
               colors=["silver"])

print(yamaha.play())
print(yamaha.colors)

lespaul = EletricGuitar("lespaul m1")
print(lespaul.play(distortion=Distortion.wave))
