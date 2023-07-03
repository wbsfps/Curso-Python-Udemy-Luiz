nome = str(input("Informe seu nome: "))
altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso em quilogramas: "))
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é:'
linha_3 = f'{imc:.1f}'
print(f"{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:,.1f}")

print(linha_1)
print(linha_2)
print(linha_3)