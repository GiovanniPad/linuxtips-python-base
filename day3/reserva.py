#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preco
1, Suite Master, 500
2, Quarto Familia, 200
3, Quarto Single, 100
4, Quarto Simples, 50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a qunatidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas.

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Bibliotecas necessárias
import os
import sys
import logging

# Logger e Handler personalizado
log = logging.Logger("reserva.py", logging.DEBUG)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Minha solução

# Colentado o caminho dos arquivos
path = os.curdir
rooms_filepath = os.path.join(os.curdir, "archives", "quartos.txt")
rents_filepath = os.path.join(os.curdir, "archives", "reservas.txt")

# Verificando se ambos os arquivos existem.
# Trata erro de permissão de acesso e arquivo não encontrado.
try:
    rented_rooms = []
    for line in open(rents_filepath):
        client_name, room_number, days_rented = line.strip().split(",")
        rented_rooms.append(int(room_number))

    available_rooms = {}
    for line in open(rooms_filepath):
        room_number, room_type, room_price = line.strip().split(",")

        room_number = int(room_number)
        room_price = float(room_price)

        if room_number not in rented_rooms:
            available_rooms[room_number] = {
                "type": room_type,
                "price": room_price # TODO: decimal
            }
except FileNotFoundError as e:
    log.critical(str(e))
    sys.exit(1)
except PermissionError as e:
    log.critical(str(e))
    sys.exit(1)


# Vefica se existe quartos disponíveis para alugar, senão encerra o programa.
if not available_rooms:
    print("Hotel lotado, volte mais tarde!")
    sys.exit(1)

# Menu principal com os quartos
print("Sistema de reserva de quarto de hotel")
print("Quartos disponíveis")
print("-" * 40)

# Exibe cada quarto com suas informações
for room_number, room_data in available_rooms.items():
    print(f"Quarto {room_number} - Tipo: {room_data["type"]} - Valor (dia): R${room_data["price"]:.2f}")
print("-" * 40)

# Pergunta o nome do cliente
client_name = input("Qual o seu nome? ")

# Loop principal, só sai se todas as informações forem inseridas corretamente.
while True:

    # Verifica se o valor inserido é numérico e se o quarto não está alugado.
    try:
        room_rent = int(input("Qual o número do quarto? "))
        if room_rent not in available_rooms:
            print("Quarto já alugado")
            continue
        days_rent = int(input("Por quantos dias vai alugar? "))
        break
    except ValueError as e:
        log.error("Valor inválido, por favor, insirar novamente.")

# Se caso tudo estiver correto, a reserva com os dados são salvas no arquivo `reservas.txt`.
with open(rents_filepath, "a") as file_:
    file_.write(f"{client_name},{room_rent},{days_rent}\n")

# Calcula o custo total de alugar o quarto.
total = available_rooms[room_rent]["price"] * days_rent

# Mensagem de confirmação exibindo o valor do aluguel do quarto.
# TODO: substituir casa decimal por vírgula
print(f"{client_name.capitalize()}, o quarto {room_rent} foi alugado com sucesso por {days_rent} dias por um total de R${total:.2f}.")



# Solução do professor
ocupados = {}
try:
    for line in open(rents_filepath):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)

quartos = {}
try:
    for line in open(rooms_filepath):
        codigo, nome, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": float(preco),
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)

print("Reserva Hotel Pythonico")
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(1)

nome = input("Nome do cliente:").strip()
print("-" * 40)
print("Lista de quartos:")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "Não disponível" if not dados["disponivel"] else "Disponível"
    #disponivel = dados["disponivel"] and "Disponível" or "Não disponível"

    print(f"{codigo} - {nome_quarto} - R$ {preco:.2f} - {disponivel}")
print("-" * 40)

try:
    quarto = int(input("Número do quarto:").strip())
    if not quartos[quarto]["disponivel"]:
        print(f"O quarto {quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas números")
    sys.exit(1)
except KeyError:
    print(f"O quarto {quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Quantos dias:").strip())
except ValueError:
    logging.error("Número inválido, digite apenas números")
    sys.exit(1)

nome_quarto = quartos[quarto]["nome"]
preco = quartos[quarto]["preco"]
disponivel = quartos[quarto]["disponivel"]
total = preco * dias

with open(rents_filepath, "a") as file_:
    file_.write(f"{nome},{quarto},{dias}\n")
    #file_.write(",".join([nome, str(quarto), str(dias)]))

print(f"{nome} você escolheu o quarto {nome_quarto} e vai custar R${total:.2f}")