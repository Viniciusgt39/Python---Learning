# Tuplas - Imutáveis
coordenadas = (10, 20)
ponto_3d = (5, 7, 9)

# Desempacotamento de tupla
x, y = coordenadas
print(f"Coordenadas: x={x}, y={y}")

# Dicionários - Pares chave-valor
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores
print(pessoa["nome"])
print(pessoa.get("profissao", "Não informada"))  # Valor padrão

# Modificando dicionário
pessoa["profissao"] = "Desenvolvedor"
pessoa["idade"] += 1

# Removendo itens
del pessoa["cidade"]
item_removido = pessoa.pop("idade")

# Métodos úteis
print(pessoa.keys())    # Chaves
print(pessoa.values())  # Valores
print(pessoa.items())   # Pares chave-valor

# Conjuntos - Coleção não ordenada sem elementos repetidos
numeros_set = {1, 2, 3, 4, 5}
numeros_set.add(6)
numeros_set.remove(3)

# Operações de conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))       # União
print(set1.intersection(set2))  # Interseção
print(set1.difference(set2))    # Diferença