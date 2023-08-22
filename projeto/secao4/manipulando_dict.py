# Manipulando chaves e valores em dicionários
person = {}

##
##

chave = 'full_name'
person[chave] = 'Luiz Otávio'
person['sobrenome'] = 'Miranda'

print(person[chave])

person[chave] = 'Maria'
del person['sobrenome']

print(person)

print(person.get('sobrenome'))

if person.get('sobrenome') is None:  # O get tenta obter uma chave
    print('Não existe')
else:
    print(person['sobrenome'])

#     print('Existe')
