# dir - retorna todas as propriedades e métodos do objeto especificado.
# hasattr - Sua principal tarefa é verificar se um objeto tem o atributo nomeado fornecido e retornar verdadeiro se presente, caso contrário, falso.
# getattr - A função é usada para acessar o valor do atributo de um objeto e também dá a opção de executar o valor padrão em caso de indisponibilidade da chave.

string = 'luiz'

metodo = 'upper'

if hasattr(string, metodo):  # ou if hasattr(string, 'upper')
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)
