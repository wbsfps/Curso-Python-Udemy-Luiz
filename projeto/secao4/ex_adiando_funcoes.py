def sum_(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def execute(function, x):
    def interna(y):
        return function(x, y)
    return interna


soma_com_cinco = execute(sum_, 5)
multiplica_por_dez = execute(multiplication, 10)
print(soma_com_cinco(10))
print(multiplica_por_dez(10))
