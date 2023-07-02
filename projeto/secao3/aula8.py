
nome = str(input("Informe seu nome: "))
sobrenome = str(input("Informe seu sobrenome: "))
idade = int(input("Informe sua idade: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))
maior_de_idade = idade >= 18
altura_metros = float(input("Informe sua altura em metros: "))

print("Nome:", nome, "Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura:", altura_metros)