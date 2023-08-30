def exec(function, *args):
    return function(*args)


def sum1(x, y):
    return x+y


def create_multiplier(multiplier):
    def multiplied(number):
        return number * multiplier
    return multiplied


# double = create_multiplier(2)
double = exec(
    lambda m: lambda n: n*m, 2
)

print(double(2))

print(exec(lambda x, y: x+y, 2, 3),
      exec(sum1, 2, 3),
      sum1(2, 3)
      )

print(exec(lambda *args: sum(args), 1, 2, 32, 3, 23, 23, 2))

double = create_multiplier(2)
print(double(4))
