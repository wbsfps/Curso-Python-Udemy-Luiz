'''
Introdução à List comprehension em Python
List comprehension é uma forma rápida para criar listas 
a partir de iteráveis 
print(list(range(10))
'''

lista = []
for number in lista:
    lista.append(number)
# print(lista)

lista = [
    number * 2
    for number in range(10)
]
print(list(range(10)))
print(lista)

# Mapeamento de dados em list comprehension
products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

news_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
]
# print(news_products)
print(*news_products, sep='\n')
