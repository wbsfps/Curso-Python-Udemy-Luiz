"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Luiz'), (2, 'Helena'), (3, 'Joao')]

lista = ['Maria', 'Luiz', 'Helena']
lista.append('Joao')

for indice, nome in enumerate(lista):
    print(indice,nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(item)

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
