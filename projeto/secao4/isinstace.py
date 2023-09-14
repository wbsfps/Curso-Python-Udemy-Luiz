# isinstance - para saber se objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name': 'William'}]


for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(10)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('str')
        print(item.upper())

    elif isinstance(item, (float, int)):
        print('num')
        print(item, item * 2)

    else:
        print('outro')
        print(item)
