# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

options = ["listar", "desfazer", "refazer"]
tasks = []
undone_tasks = []

def clean():
    os.system("cls")

def add_item(item):
    tasks.append(item)
    undone_tasks.clear()
    return tasks
def undo():
    if tasks:
        removed_item = tasks.pop()
        undone_tasks.append(removed_item)
    else: 
        print("Nada para desfazer")
    return tasks

def redo(item):
    if undone_tasks:
        tasks.append(item)
    else:
        print("Nada para refazer")
    return tasks

while True:
    option = input(f"Comandos: listar, desfazer, refazer: ")

    if option not in options:
        clean()
        print(add_item(option))    
    
    elif option == options[0]:
        clean()
        print("Listagem...", tasks)
    
    elif option == options[1]:
        clean()
        print(undo()) 
    
    elif option == options[2]:
        clean()
        print(redo())
    
    exit = input("Deseja sair? (s/n): ").lower().strip()
    if exit == "s".lower().strip():
        break