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

p1 = {
    'name': 'William',
    'age': 18,
    'surname': 'Batista'
}

# print(p1['name'])
# print(p1.get('name', 'não existe'))

# nome = p1.pop('name')
# print(nome)
# print(p1)

# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)

# p1.update({
#     'name': 'novo valor',
#     'age': 20
# })

# print(p1)

# p1.update(name='novo valor', age=30)
# print(p1)

# tupla = (('nome', 'novo valor'), ('idade', 18))
lista = [['nome', 'novo valor'], ['idade', 18]]
# p1.update(tupla)
p1.update(lista)
print(p1)
