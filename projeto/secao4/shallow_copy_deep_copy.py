# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# Cópia rasa (shallow copy)
d2 = copy.copy(d1)
d2['c1'] = 1000
d2['l1'][1] = 40  # Modifica a lista original
print("Shallow Copy:")
print("d1:", d1)
print("d2:", d2)

print()

# Redefinir d1 para evitar influência da primeira modificação
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# Cópia profunda (deep copy)
d2 = copy.deepcopy(d1)
d2['c1'] = 1000
d2['l1'][1] = 40  # NÃO modifica a lista original
print("Deep Copy:")
print("d1:", d1)
print("d2:", d2)
