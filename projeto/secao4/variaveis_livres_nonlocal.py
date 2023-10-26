# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def out(x):
#     a = x

#     def in_():
#         print(locals()) # vendo variáveis locais
#         print(in_.__code__.co_freevars) # vendo variáveis livres
#         return a
#     return in_


# dentro1 = out(1)
# dentro2 = out(12)
# print(dentro1(), dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final  # pegando o valor_final por não estar no escopo da função interna
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
