'''

Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update    Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''
#        0   1   2   3
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)  # adiciona algum elemento na última posição da lista
lista.pop()  # remove o último elemento da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)  # o valor que colocar no pop precisa ser o índice
print(lista, 'Removido,', ultimo_valor)