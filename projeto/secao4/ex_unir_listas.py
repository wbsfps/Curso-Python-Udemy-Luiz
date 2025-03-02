# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(states=None, federal_unit=None):
    def decorator(func):
        def union_lists(*args, **kwargs):
            res = func(*args, **kwargs)
            final = tuple(zip(*res))
            return final
        return union_lists
    return decorator

@zipper()
def lists():
    return ('Salvador', 'Ubatuba', 'Belo Horizonte'), ('BA', 'SP', 'MG', 'RJ')

print(lists())