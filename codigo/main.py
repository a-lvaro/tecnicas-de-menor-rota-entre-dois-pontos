import tkinter as tk
from rota import Rota

'''equipe:
        Álvaro de Araújo Ferreira Lima Neto
        Rafael Prado Torres
        
    professor:
        Wagner Igarashi
        
    matéria:
        IA I'''


def display_grafoPequeno():
    next_window = tk.Toplevel(root)
    next_window.title("Grafo Pequeno")
    next_window.geometry("400x200+300+300")
    text = '''começaremos com a busca em um grafo menor
    \nEsse grafo possui 263 vértices'''
    next_label = tk.Label(next_window, text=text)
    next_label.pack()

    rotamenor = Rota("pequena")

    tk.Button(next_window, text="Rota",
              command=rotamenor.mostrarPontos).pack(side=tk.LEFT)
    tk.Button(
        next_window, text="A*", command=rotamenor.bucaAestrela).pack(side=tk.LEFT)
    tk.Button(next_window, text="Aprofundamento Iterativo",
              command=rotamenor.buscaAprofundamentoIterativo).pack(side=tk.LEFT)
    tk.Button(next_window, text="Voltar",
              command=next_window.destroy).pack(side=tk.RIGHT)


def display_grafoMedio():
    next_window = tk.Toplevel(root)
    next_window.title("Grafo médio")
    next_window.geometry("400x200+300+300")
    text = '''Agora, iremos fazer a busca em um grafo médio
    \nEsse grafo possui 1849 vértices'''
    next_label = tk.Label(next_window, text=text)
    next_label.pack()

    rotamenor = Rota("media")

    tk.Button(next_window, text="Rota",
              command=rotamenor.mostrarPontos).pack(side=tk.LEFT)
    tk.Button(
        next_window, text="A*", command=rotamenor.bucaAestrela).pack(side=tk.LEFT)
    tk.Button(next_window, text="Aprofundamento Iterativo",
              command=rotamenor.buscaAprofundamentoIterativo).pack(side=tk.LEFT)
    tk.Button(next_window, text="Voltar",
              command=next_window.destroy).pack(side=tk.RIGHT)


def display_grafoGrande():
    next_window = tk.Toplevel(root)
    next_window.title("Grafo Grande")
    next_window.geometry("400x200+300+300")
    text = '''Agora, iremos fazer a busca em um grafo grande
    \nEsse grafo possui 9563 vértices'''
    next_label = tk.Label(next_window, text=text)
    next_label.pack()

    rotamenor = Rota("grande")

    tk.Button(next_window, text="Rota",
              command=rotamenor.mostrarPontos).pack(side=tk.LEFT)
    tk.Button(
        next_window, text="A*", command=rotamenor.bucaAestrela).pack(side=tk.LEFT)
    tk.Button(next_window, text="Aprofundamento Iterativo",
              command=rotamenor.buscaAprofundamentoIterativo).pack(side=tk.LEFT)
    tk.Button(next_window, text="Voltar",
              command=next_window.destroy).pack(side=tk.RIGHT)


root = tk.Tk()
root.title("Apresentação")
root.geometry("500x200+300+300")
text = '''Trabalho de IA, busca do menor caminho entre dois pontos em um mapa
\nAlunos:  Álvaro de Araújo, Rafael Torres 
\n\nNesse trabalho, iremos achar a menor rota entre dois pontos em um mapa
\n\nos algoritmos usados são A* e Aprofundamento Iterativo'''

info_label = tk.Label(root, text=text)
info_label.pack()

tk.Button(root, text="Grafo Pequeno",
          command=display_grafoPequeno).pack(side=tk.LEFT)
tk.Button(root, text="Grafo Médio",
          command=display_grafoMedio).pack(side=tk.LEFT)
tk.Button(root, text="Grafo Grande",
          command=display_grafoGrande).pack(side=tk.LEFT)
tk.Button(root, text="Sair", command=root.destroy).pack(side=tk.RIGHT)


root.mainloop()
