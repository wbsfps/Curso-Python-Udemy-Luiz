# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def double(number):
#     return number * 2
# def triple(number):
#     return number * 3
# def quadruple(number):
#     return number * 4

# print_double = double
# print_triple = triple
# print_quadruple = quadruple

# print(print_double(2))
# print(print_double(100))


def create_multiplier (multiplicador):
    def multiply (numero):
        return multiplicador * numero
    return multiply

double = create_multiplier(2)
triplicar = create_multiplier(3)
quadruplicar = create_multiplier(4)

print(double(2))
print(triplicar(2))
print(quadruplicar(2))