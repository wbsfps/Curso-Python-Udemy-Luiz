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

path =  "./projeto/secao4/criando_arquivos_com_python_context_manager_with.txt"
with open(path, "w") as file:
    file.write("Hello, World!")
    print(f"File created in: {path}")
    file.close()