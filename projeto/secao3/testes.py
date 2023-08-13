while True:
    numero_1 = input('Informe um número: ')
    numero_2 = input('Informe outro número: ')
    opcao = input('Informe a operação que você quer fazer: + - / % * ')
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)

    soma = '+' 
    subtracao = '-'
    multi = '*'
    div = '/'
    modulo = '%'

    operadores_permitidos = '+-/%'

    if opcao not in operadores_permitidos:
        print('Operador inválido')
        break 

    if len(opcao) > 1:
        print('Digite apenas um operador!')
        continue

    if opcao == soma:
        print(f'{numero_1_float + numero_2_float}')
    elif opcao == subtracao:
        print(f'{numero_1_float - numero_2_float}')
    elif opcao == multi:
        print(numero_1_float * numero_2_float)
    elif opcao == div:
        print(numero_1_float / numero_2_float)
    elif opcao == modulo:
        print(numero_1_float % numero_2_float)
    else: 
        print('Não conheço essa operação')

    continuar_ou_nao_o_programa = input('Deseja continuar? [s]im ou [n]ão ')
    continuar = ''.startswith('s')
    sair = ''.startswith('n')

    if continuar_ou_nao_o_programa == continuar:
        continue
    else: break
    
print('Fim do programa!')