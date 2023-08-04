"""
Exercício 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Luiz', 'Helena']
lista.append('Joao')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])