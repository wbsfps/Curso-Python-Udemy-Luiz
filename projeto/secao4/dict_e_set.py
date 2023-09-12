# Dictionary Comprehesion e Set Comprehesion

product = {
    'name': 'blue pen',
    'price': 2.5,
    'category': 'desk'
}

for key, value in product.items():
    print(key, value)

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'category'
}

lista = [{
    ('a', 'value a'),
    ('b', 'valor a'),
    ('b', 'valor a')
}]

dc = {
    key: value
    for key, value in lista
}
print(dc)


s1 = {(2 ** i)for i in range(10)}

print(s1)
