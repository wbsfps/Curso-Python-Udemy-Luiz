'''

Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final 
    insert - Adiciona um item no índice escolhido 
    pop - Remove do final ou do índice escolhido 
    del - Apaga um índice 
    clear - Limpa a lista 
    extend - Estende a lista 
    + - concatena a lista
Create Read Update    Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(1, 5)
print(lista[5])