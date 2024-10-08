# Paradigma Imperativo/Procedural
# Objeto do tipo dicionário para armazenar dados
people = [
    {
        "name": "Jim Halpert",
        "balance": 500,
        "role": "Salesman"
    },
    {
        "name": "Dwight Schrute",
        "balance": 100,
        "role": "Manager"
    }
]


# Função para adicionar pontos
def add_points(person, value):
    # Cria uma cópia do objeto que vai ser alterado, evitando side effects
    data = person.copy()  # no side effects
    if data["role"] == "Manager":
        value *= 2
    data["balance"] += value
    return data


# Paradigma Funcional
# Declarativa
# Lazy evaluation, enquanto o objeto não for consumido,
# ele não vai ser executado
result = map(lambda person: add_points(person, 100), people)

# Consumindo (executando) o objeto map `result`
print(f"Dicionário Cópia: {list(result)}")

# Imprimindo o dicionário original
print(f"Dicionário original: {people}")

# Pode-se ver no resultado que o dicionário original não teve alterações,
# apenas a sua cópia foi alterada, evitando side effects
