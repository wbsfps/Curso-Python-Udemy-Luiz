'''
Flag(Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Indentidade
'''
# variavel = 'a'
# print(id(variavel))


condicao = False
passouNoIf = None

if condicao:
    passouNoIf = True
    print("Faça algo")
else:
    print('Não faça algo')

if passouNoIf is None:
    print("Não passou no if")
if passouNoIf is not None:
    print("Passou no if")

'''
ou
if passouNoIf is None:
    print("Não passou no if")
else:
    print("Passou no if")

'''