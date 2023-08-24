lista = []
for i in range(1, 5):
    grades = input('Informe a nota: ')
    grades_float = float(grades)
    lista.append(grades_float)

media = sum(lista) / len(lista)

print(lista)
print(media)
