import osmnx as ox
import matplotlib.pyplot as plt

from funcoes import recuperarCaminho


def mostrarPontosNoGrafo(grafo, noInicio, noFim):
    fig, ax = ox.plot_graph(grafo, show=False, close=False)
    ax.scatter(grafo.nodes[noInicio]['x'], grafo.nodes[noInicio]['y'], c='red')
    ax.scatter(grafo.nodes[noFim]['x'], grafo.nodes[noFim]['y'], c='red')
    ax.set_title('ponto de ínicio e fim da rota')
    fig.suptitle('grafo')
    plt.show()


def mostrarCaminho(arvore, grafo, tipoBusca):
    caminho, custo = recuperarCaminho(arvore)

    fig, ax = ox.plot.plot_graph_route(grafo, caminho, show=False, close=False)
    ax.set_title('custo: ' + str(round(custo, 2)) + 'm')
    fig.suptitle(tipoBusca)

    plt.show()
