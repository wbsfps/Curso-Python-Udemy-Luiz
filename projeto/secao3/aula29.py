"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
"""

numero_str = (input("Informe um número: "))

try:
     print('Str:', numero_str)
     numero_float = float(numero_str)
     print('Float:', numero_float)
     print(f"O dobro de {numero_str} é {numero_float * 2:.1f}")
except:
     print("Isso não é um número")

# if numero_str.isdigit() :

#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.1f}")
# else:
#     print("Isso não é um número")