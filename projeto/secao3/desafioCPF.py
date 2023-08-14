"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

lista_dos_numeros = []
lista_da_soma_com_os_numeros_ja_multiplicados = []

for i in range(1, 10):
    numeros_cpf = input('Informe um número: ')
    numeros_int = int(numeros_cpf)

    if len(numeros_cpf) > 1:
        break

    lista_dos_numeros.append(numeros_int)
    soma_dos_primeiros_digitos = sum(lista_dos_numeros)

multiplicando_primeiro_digito = lista_dos_numeros[0] * 10
multiplicando_segundo_digito = lista_dos_numeros[1] * 9
multiplicando_terceiro_digito = lista_dos_numeros[2] * 8
multiplicando_quarto_digito = lista_dos_numeros[3] * 7
multiplicando_quinto_digito = lista_dos_numeros[4] * 6
multiplicando_sexto_digito = lista_dos_numeros[5] * 5
multiplicando_setimo_digito = lista_dos_numeros[6] * 4
multiplicando_oitavo_digito = lista_dos_numeros[7] * 3
multiplicando_nono_digito = lista_dos_numeros[8] * 2

resultados = multiplicando_primeiro_digito, multiplicando_segundo_digito, multiplicando_terceiro_digito, multiplicando_quarto_digito, multiplicando_quinto_digito, multiplicando_sexto_digito, multiplicando_setimo_digito, multiplicando_oitavo_digito, multiplicando_nono_digito


soma_dos_resultados = sum(resultados)

multiplicando_soma_dos_resultados_por_dez = soma_dos_resultados * 10

obter_resto_da_divisao = multiplicando_soma_dos_resultados_por_dez % 11

digito = obter_resto_da_divisao

digito = digito if digito <= 9 else 0

print(soma_dos_primeiros_digitos)
print(multiplicando_soma_dos_resultados_por_dez)
print(soma_dos_resultados)
print(digito)
