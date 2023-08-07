import os
lista_de_compras = []

while True:
        opcao = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar: ')
        if opcao == 'i':
            valor = input('Valor: ')
            lista_de_compras.append(valor)
        elif opcao == 'a':
            indice_str = input('Escolha o índice para apagar: ')
            try:
                indice = int(indice_str)
                del lista_de_compras[indice]
            except ValueError: print('Por favor digite número int.')
            except IndexError: print('Índice não existe') 
            except Exception: print('Erro desconhecido')
        elif opcao == 'l':
            os.system('clear')

            if len(lista_de_compras) == 0:
                print('Não tem nada para listar')
            for i, valor in enumerate(lista_de_compras):
                print(i, valor)
        else:
            print('Verifique a opção que você solicitou. Pois, ela não foi compatível')