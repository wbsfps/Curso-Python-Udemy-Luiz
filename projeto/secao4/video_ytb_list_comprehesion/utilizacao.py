def divisionfn(x, y):
    return x / y


def multiplicationfn(x, y):
    return x * y


def squarefn(x, y):
    return x ** y


numbers = [1, 2, 3, 4, 5]
division = [divisionfn(number, 2) for number in numbers]
multiplication = [multiplicationfn(number, 2)for number in numbers]
square = [squarefn(number, 2) for number in numbers]

print(numbers)
print(division)
print(multiplication)
print(square)
