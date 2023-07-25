'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o iterador
'''
# texto = iter('Luiz') #.__iter__()

# print(next(texto)) #.__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))

#for letra in texto

texto = 'Luiz' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto:
    print(letra)