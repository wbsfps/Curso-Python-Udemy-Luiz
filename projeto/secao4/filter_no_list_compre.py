import pprint


def p(v):
    pprint.pprint(news_products, sort_dicts=False, width=40)


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
# print(*news_products, sep='\n')
# p(news_products)

# lista = [n for n in range(10) if n < 5]
# print(lista)

news_products = [
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 20 else {**product}
    for product in products
    if (product['price'] >= 20 and product['price'] * 1.05) > 10
]
p(news_products)

# Mapeamento quer dizer que eu estou pegando um dado.
# E jogando numa outra lista
# E essas duas listas tem o mesmo tamanho

# Filtro quer dizer que eu posso ou não incluir aquele elemento na lista
