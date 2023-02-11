import osmnx as ox
from vertice import Vertice
from funcoes import custo

# distância em linha reta do vértice atual ao vértice fim


def heuristica(grafo, u, v):
    return ox.distance.great_circle_vec(grafo.nodes[u]['x'], grafo.nodes[u]['y'], grafo.nodes[v]['x'], grafo.nodes[v]['y'], earth_radius=6371009)


def buscaAestrela(grafo, dfGrafo, inicio, fim):
    def ordenarPeloCusto(encontrarVizinhos): return encontrarVizinhos.sort(
        key=lambda x: x.getCusto() + x.getHeuristica())
    encontrarVizinhos = []
    arvore = []
    nosJaPercorridos = [inicio]

    encontrarVizinhos.append(
        Vertice(inicio, None, 0, heuristica(grafo, inicio, fim)))

    while encontrarVizinhos != [] and (arvore[-1].getIdNo() != fim if arvore != [] else True):
        atual = encontrarVizinhos.pop(0)
        arvore.append(atual)

        for adjacente in grafo.adj[atual.getIdNo()]:
            if adjacente not in nosJaPercorridos:
                nosJaPercorridos.insert(0, adjacente)
                encontrarVizinhos.append(Vertice(adjacente, atual.getIdNo(), custo(
                    dfGrafo, atual, adjacente), heuristica(grafo, adjacente, fim)))

        ordenarPeloCusto(encontrarVizinhos)

    if encontrarVizinhos == []:
        print(f'\n\nnó {fim} não encontrado\n\n')

    return arvore
