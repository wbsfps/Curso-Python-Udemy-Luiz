"""
Higher Order Functions
Funções de primeira classe
"""


def salutation(msg, nome):
    return f'{msg}, {nome}!'




def exec(function, *args):
    return function(*args)


exec(salutation, 'Bom dia', 'William')

print(exec(salutation, 'Bom dia', 'William'))
print(exec(salutation, 'Bom dia', 'Maria'))
