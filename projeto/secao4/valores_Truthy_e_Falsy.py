# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

lista = []
dicionario = {}
conjunto = set()
inteiro = 0
flutuante = 0.0
tupla = ()
string = ''
falso = False
intervalo = range(10)
nada = None


def falsy(value):
    return 'falsy' if not value else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{intervalo=}', falsy(intervalo))
print(f'{nada=}', falsy(nada))
