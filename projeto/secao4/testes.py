# # Questão 1
# # Funções Básicas:
# # a) Escreva uma função que calcule e retorne o quadrado de um número.
# import datetime


# def square(number):
#     return number ** 2


# print_square = square
# print(square(39))

# # b) Crie uma função que determine se um número é par ou ímpar.


# def check_parity(number):
#     if number % 2 == 0:
#         return 'par'
#     else:
#         return 'impar'


# print(check_parity(4))
# print(check_parity(5))
# # c) Implemente uma função que calcule a média de uma lista de números.


# def listen(numbers):
#     media = sum(numbers) / len(numbers)
#     return media


# print(listen(numbers=[1, 2, 4, 56, 6, 7, 32]))

# # Questão 2
# # Parâmetros e Retorno:
# # a) Crie uma função que receba dois números e retorne o maior deles.


# def biggest(n1, n2):
#     if n1 > n2:
#         return f'{n1}'
#     return f'{n2}'


# print(biggest(4, 2))
# # b) Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.


# def sum_list(lista):
#     soma = sum(lista)
#     return soma


# print(sum_list(lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# # c) Implemente uma função que aceite uma string e um número, e retorne a string repetida o número de vezes especificado.


# def string(string):
#     def multiply(number):
#         return string * number
#     return multiply


# multiplicador_string = string('a')
# print(multiplicador_string(10))

# # Questão 3
# # Funções Recursivas:
# # a) Defina uma função recursiva para calcular o fatorial de um número.


# def factorial(numero):
#     total = 1
#     for num in range(1, numero + 1):
#         total *= num
#     return total


# print(factorial(4))

# # b) Escreva uma função recursiva para calcular o N-ésimo termo da sequência de Fibonacci.
# # c) Implemente uma função recursiva para calcular o MDC (Máximo Divisor Comum) de dois números.

persons = [
    {
        'name': 'Pedro',
        'age': 23,
    },
    {
        'name': 'William',
        'age': 18
    },
    {
        'name': 'CJ',
        'age': 25
    }
]

# for name in persons:
#     print('Nome: ', name['name'])

# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]


# def find_first_duplicate(list_of_interable):

#     numbers_checks = set()
#     first_duplicate = -1

#     for number in list_of_interable:
#         if number in numbers_checks:
#             number = first_duplicate
#             break
#         numbers_checks.add(number)
#         print()
#     return first_duplicate


# for list in lista_de_listas_de_inteiros:
#     print(list, find_first_duplicate(list))


