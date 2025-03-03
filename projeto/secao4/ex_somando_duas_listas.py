
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# Meu
from itertools import zip_longest

def sum_lists(l1, l2):
    interval = min(len(l1), len(l2))
    return [
        l1[i] + l2[i] for i in range(interval)
    ]

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(sum_lists(l1, l2))
print(list(zip(l1, l2)))
print(list(zip_longest(l1,l2)))

""" 
Vídeo - Primeira forma
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

print()

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)

""" 
Vídeo - Segunda forma
"""
print()

lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

""" 
Vídeo - Terceira forma
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x, y for x, y in zip(lista_a, lista_b)]
print(lista_soma)