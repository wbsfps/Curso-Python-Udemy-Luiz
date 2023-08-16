"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""


# def Print(a, b, c):
#     print(a)
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')


saudacao('William')
saudacao('Maria')
saudacao('Helena')
saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16,8)