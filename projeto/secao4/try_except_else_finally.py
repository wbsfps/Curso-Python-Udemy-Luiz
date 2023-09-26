# try, except, else e finally
# Parte 3

# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# O try e finally sempre serão executados

try:
    print('Abrir arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero')
except IndexError as error:
    print('IndexError')
except TypeError:
    print('TypeError')
except (NameError, ImportError):
    print('NameError + ImportError')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
