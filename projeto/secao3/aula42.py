frase = 'aaaaooo'


i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atuual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atuual:
        qtd_apareceu_mais_vezes = qtd_atuual
        letra_que_apareceu_mais_vezes = letra_atual
    i += 1

print(
    f'A letra que apareceu mais vezes foi: {letra_que_apareceu_mais_vezes} que apareceu {qtd_apareceu_mais_vezes}x')
