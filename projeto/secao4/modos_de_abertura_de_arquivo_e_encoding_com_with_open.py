# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# windows_path_example = "C:\\Users\\willi\\OneDrive\\Documentos\\github\\Curso-Python-Udemy-Luiz\\projeto\\secao4\\"
# linux_mac_path_example = "/Users/william/criando_arquivos_com_python_context_manager_with.txt"

# file = open(windows_path_example, "w")
# file.close()

path =  "./projeto/secao4/modos_de_abertura_de_arquivo_e_encoding_com_with_open.txt"
# with open(path, "w+") as file:
    
#     file.write("Row 1! \n")
#     file.write("Row 2! \n")
#     file.write("Row 3! \n")
#     file.writelines(
#         ("Row 4! \n", "Row 5! \n", "Row 6! \n")
#     )
#     file.seek(0, 0)

#     print(file.read())
#     print("Read")
#     file.seek(0, 0)
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     print(file.readline(), end="")
#     print(file.readline(), end="")

#     print("Readlines")
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())
#     file.close()

# with open(path, "r") as file:
#     print(file.read())

with open(path, "w+", encoding="utf-8") as file:
    file.write("Atenção")
    file.write("Row 1! \n")
    file.write("Row 2! \n")
    file.write("Row 3! \n")
    file.writelines(
        ("Row 4! \n", "Row 5! \n", "Row 6! \n")
    )

    file.close()