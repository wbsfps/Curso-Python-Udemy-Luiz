# raise - lançamento de exceções (erros)

# def division(number, divider):
#     try:
#         return number / divider
#     except ZeroDivisionError:
#         print('____')
#         raise  # relançando o erro
#         # return number


# print(division(8, 0))


# def division(number, divider):
#     if divider == 0:
#         raise ZeroDivisionError('Não é possível fazer essa divisão')
#     return number / divider


# # print(division(8, 0))
# print(round(division(8, 3), 2))
# print(round(division(8, 5), 2))

def not_accept_zero(divider):
    if divider == 0:
        raise ZeroDivisionError('Não é possível fazer essa divisão')
    return True


def deve_ser_int_ou_float(number, divider):
    tipo_n = type(number)
    if not isinstance(number, (float, int)):
        raise TypeError(f'"{number}" deve ser int ou float ',
                        f'"{tipo_n.__name__}" enviado')

    tipo_d = type(divider)
    if not isinstance(divider, (float, int)):
        raise TypeError(f'{divider} deve ser int ou float ')

    return True


def division(number, divider):
    deve_ser_int_ou_float(number, divider)
    not_accept_zero(divider)
    return number / divider


print(round(division('6', 3), 2))
print(round(division(6, '3'), 2))
print(round(division(2, 0), 2))
