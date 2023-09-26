# Try, excepty, else e finally
# Parte 1 e 2

# a = 18
# b = 0
# print('linha 1')
# c = a / b

# b = 0
# print(b[0])

try:
    a = 18
    b = 0
    # print(b[0])
    print('linha 1'[1000])
    c = a / b
    print('linha 2')
except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('msg', error)  # descobrindo o tipo de erro
    print('Nome:', error.__class__.__name__)  # achando o nome do erro
except Exception:
    print('Erro desconhecido.')


print('Continuar')
