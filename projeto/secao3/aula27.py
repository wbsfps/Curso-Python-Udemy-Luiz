'''
Fatiamento de strings
 012345678
 Olá mundo
 -987654321
 Fatiamento [i:f:p] [::]
 Obs.: a função len retorna a quantidade de caracteres
'''
variavel = 'Olá mundo'.strip()
print(variavel[0:5:])
print(variavel[::-1])
print(variavel[:2:-1])
print(len(variavel))
print(variavel[0:len(variavel):1]) # == print(variavel[0:9:2])