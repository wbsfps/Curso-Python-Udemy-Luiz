lista = []
for i in range(1, 11):
    numbers = input('Informe um número: ')
    numbers_int = int(numbers)
    lista.append(numbers_int)
    lista.sort(reverse=True)
print(lista)
