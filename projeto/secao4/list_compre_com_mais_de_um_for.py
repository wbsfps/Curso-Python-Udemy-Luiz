lista = []
for x in range(3):
    for y in range(3):
        # para adicionar dois elementos na lista precisa colocar numa tupla
        lista.append((x, y))

lista = [{
    (x, y)
    for x in range(3)
    for y in range(3)
}]

lista = [{
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
}]

print(lista)
