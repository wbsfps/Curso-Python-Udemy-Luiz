# Operadores in e not in 
# Strings são iteráveis
#  0 1 2 3 4 5 
#  O t á v i o
# -6-5-4-3-2-1 
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('zero' in nome)
# print('-' * 10)
# print('zero' not in nome)
# print('vio' not in nome)]

nome = input("Informe seu nome: ")
encontrar = input("Digite o que deseja entrar")
if encontrar in nome:
    print(f'{encontrar} está em nome')
else:
    print(f'{encontrar} não está em {nome}')