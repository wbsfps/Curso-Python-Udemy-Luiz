# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

s1 = {1, 2, 3}
# print(3 in s1)

# for number in s1:
#     print(number)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Luiz')
s1.add(1)


s1.update(('Olá mundo!', 1, 2, 3, 4, 5)) # Para mandar mais de um valor utilizar parenteses

 
# s1.clear()
# Como o set não possui indexes, para remover algum item basta colocar o item que deseja remover

s1.discard(3)
print(s1)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
