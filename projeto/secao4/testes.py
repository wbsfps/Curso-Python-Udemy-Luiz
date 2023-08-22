# Questão 1
# Funções Básicas:
# a) Escreva uma função que calcule e retorne o quadrado de um número.
def square(number):
    return number ** 2


print_square = square
print(square(39))

# b) Crie uma função que determine se um número é par ou ímpar.


def check_parity(number):
    if number % 2 == 0:
        return 'par'
    else:
        return 'impar'


print(check_parity(4))
print(check_parity(5))
# c) Implemente uma função que calcule a média de uma lista de números.


def listen(numbers):
    media = sum(numbers) / len(numbers)
    return media


print(listen(numbers=[1, 2, 4, 56, 6, 7, 32]))

# Questão 2
# Parâmetros e Retorno:
# a) Crie uma função que receba dois números e retorne o maior deles.


def biggest(n1, n2):
    if n1 > n2:
        return f'{n1}'
    return f'{n2}'


print(biggest(4, 2))
# b) Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.


def sum_list(lista):
    soma = sum(lista)
    return soma


print(sum_list(lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# c) Implemente uma função que aceite uma string e um número, e retorne a string repetida o número de vezes especificado.


def string(string):
    def multiply(number):
        return string * number
    return multiply


multiplicador_string = string('a')
print(multiplicador_string(10))

# Questão 3
# Funções Recursivas:
# a) Defina uma função recursiva para calcular o fatorial de um número.


def factorial(numero):
    total = 1
    for num in range(2, numero + 1):
        total *= num
    return total


print(factorial(4))

# b) Escreva uma função recursiva para calcular o N-ésimo termo da sequência de Fibonacci.
# c) Implemente uma função recursiva para calcular o MDC (Máximo Divisor Comum) de dois números.
