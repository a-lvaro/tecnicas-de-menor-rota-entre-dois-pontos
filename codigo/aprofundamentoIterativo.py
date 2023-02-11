from vertice import Vertice
from funcoes import custo

def buscaAprofundamentoIterativo(grafo, dfGrafo, inicio, fim, profundidade):
    arvore = []
    listaAdjacencia = [Vertice(inicio, None, 0, profundidade=0)]
    nosJaPercorridos = [inicio]

    while listaAdjacencia != [] and (arvore[-1].getIdNo() != fim if arvore != [] else True):
        vertice = listaAdjacencia.pop(0)
        arvore.append(vertice)

        if vertice.getProfundidade() < profundidade:
            for adjacente in grafo.adj[vertice.getIdNo()]:
                if adjacente not in nosJaPercorridos:
                    nosJaPercorridos.insert(0, adjacente)
                    listaAdjacencia.append(Vertice(adjacente, vertice.getIdNo(), custo(
                        dfGrafo, vertice, adjacente), profundidade=vertice.getProfundidade() + 1))

    encontrou = True if arvore[-1].getIdNo() == fim else False

    return arvore, encontrou