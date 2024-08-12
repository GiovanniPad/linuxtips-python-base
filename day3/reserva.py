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
__license__ = "Unlicense"

# Bibliotecas necessárias
import os
import sys
import logging

# Colentado o caminho dos arquivos
path = os.curdir
rooms_filepath = os.path.join(path, "archives", "quartos.txt")
rents_filepath = os.path.join(path, "archives", "reservas.txt")

# Solução do professor

ocupados = {}
try:
    for line in open(rents_filepath):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome_cliente,
            "dias": int(dias)
        }
except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe")
    sys.exit(1)

# TODO: Usar função para ler os arquivos

quartos = {}
try:
    for line in open(rooms_filepath):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome": nome_quarto,
            "preco": float(preco), # TODO: decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe")
    sys.exit(1)

print("Reserva no Hotel Pythonico da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel está lotado, volte depois.")
    sys.exit(0)

nome_cliente = input("Qual é o seu nome:").strip()
print()

# TODO: Usar rich.Table
print("Lista de quartos")
print()
head = ["Número", "Nome do Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "⛔" if not dados_quarto["disponivel"] else "👍"
    #disponivel = dados["disponivel"] and "Disponível" or "Não disponível"

    print(f"{num_quarto:<6} - {nome_quarto:<14} - " f"R$ {preco:<9.2f} - {disponivel:<10}")

print("-" * 52)

try:
    num_quarto = int(input("Número do quarto:").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado, escolha outro.")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido, digite apenas números")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(1)

try:
    dias = int(input("Quantos dias:").strip())
except ValueError:
    logging.error("Número inválido, digite apenas números")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco = quartos[num_quarto]["preco"]
total = preco * dias

print(
    f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} "
    f"o valor total estimado será R$ {total:.2f}"
)

if input("Confirma? (digite y)").strip().lower() in ("y", "yes", "sim", "s"):
    with open(rents_filepath, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")