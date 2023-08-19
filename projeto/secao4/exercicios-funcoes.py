# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplied_numbers(*args):
    total = 1
    for number in args:
        total *= number
    return total


multiply = multiplied_numbers(1, 23, 4)
print(multiply)

# Crie uma função fala se um numero é par ou ímpar.
# Retorne se um número é par ou ímpar.


def check_parity(number):
    multiple_of_two = number % 2 == 0

    if multiple_of_two:
        return f'{number} é par'
    return f'{number} é ímpar'


print(check_parity(2))
print(check_parity(4))
print(check_parity(27))
print(check_parity(99))