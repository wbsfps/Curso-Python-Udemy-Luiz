'''calculadora'''
while True:
    numero_1 = input('Informe um numero: ')
    numero_2 = input("Informe outro número: ")
    operador = input('Qual operção você quer fazer? (+-/*): ')
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
        if operador == '+':
            print(numero_1_float + numero_2_float)
        elif operador == '-':
            print(numero_1_float - numero_2_float)
        elif operador == '/':
            print(numero_1_float / numero_2_float)
        elif operador == '*':
            print(numero_1_float * numero_2_float)
        else:
            print('Não conheço essa operação')

    except:
        numeros_validos = None
        if numeros_validos is None:
            print('Um ou ambos números digitados são inválidos.')
            continue
    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    if sair is True:
        break

print('---------------------------------------------------------')
# while True:
#     numero_1 = input('Digite um número: ')
#     numero_2 = input('Digite outro número: ')
#     operador = input('Digite o operador (+-/*): ')

#     numeros_validos = None

#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numeros_validos = True
#     except:
#         numeros_validos = None

#     if numeros_validos is None:
#         print('Um ou ambos os números digitados são inválidos.')
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print('Operador inválido.')
#         continue

#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue

#     ###

#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         break