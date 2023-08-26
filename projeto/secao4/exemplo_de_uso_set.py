# Exemplo de uso set
letras = set()
while True:
    letra = input('Informe uma letra: ')

    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break
    print(letras)
