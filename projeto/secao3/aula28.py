'''
Exercício
'''
nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    if ' ' in nome:
        print(f"Seu nome contêm espaços")
    else:
        print("Seu nome não contêm espaços")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")