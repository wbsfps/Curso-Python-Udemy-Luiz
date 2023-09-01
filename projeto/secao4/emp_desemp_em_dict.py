# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

person = {
    'name': 'Aline',
    'sobrenome': 'Souza'
}

# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# for key, value in person.items():
#     print(key, value)

person = {
    'name': 'Aline',
    'sobrenome': 'Souza'
}

data_person = {
    'age': 16,
    'height': 1.6
}  # empacotamento

complete_person = {**person, **data_person}  # desempacotamento

# print(complete_person)

# args e kwargs
# (args) já vimos
# kwargs - keywords arguments (argumentos nomeados)


def show_arguments_nominated(*args, **kwargs):
    print('Não nomeados:', args)
    for key, value in kwargs.items():
        print(key, value)


# show_arguments_nominated(1, 2, nome='Joana', qlq=123)
# show_arguments_nominated(**complete_person)

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}
show_arguments_nominated(**configs)
