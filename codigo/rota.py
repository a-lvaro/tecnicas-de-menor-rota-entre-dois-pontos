import osmnx as ox

from visualizarGrafo import mostrarPontosNoGrafo, mostrarCaminho
from funcoes import grafoDataFrame
from aestrela import buscaAestrela
from aprofundamentoIterativo import buscaAprofundamentoIterativo


class Rota:
    def __init__(self, opcaoRota: str):

        if opcaoRota == 'pequena':
            self.noInicio = 900551253
            self.noFim = 8794056279

            self.grafo_inga = ox.graph_from_bbox(-23.418168, -23.425714, -
                                                 51.943336, -51.933149, network_type='drive')

        elif opcaoRota == 'media':
            self.noInicio = 8859042730
            self.noFim = 1415538243

            self.grafo_inga = ox.graph_from_address('Maringá, PR, Brazil')

        elif opcaoRota == 'grande':
            self.noInicio = 8935599411
            self.noFim = 1446028511

            self.grafo_inga = ox.graph_from_bbox(
                -23.393388, -23.442619, -51.962653, -51.892584, network_type='drive')

        self.dfGrafo = grafoDataFrame(self.grafo_inga)

    def mostrarPontos(self):
        mostrarPontosNoGrafo(self.grafo_inga, self.noInicio, self.noFim)

    def bucaAestrela(self):
        arvore = buscaAestrela(
            self.grafo_inga, self.dfGrafo, self.noInicio, self.noFim)
        mostrarCaminho(arvore, self.grafo_inga, "A*")

    def buscaAprofundamentoIterativo(self):
        profundidade = 0
        encontrou = False

        while encontrou == False:
            arvore, encontrou = buscaAprofundamentoIterativo(
                self.grafo_inga, self.dfGrafo, self.noInicio, self.noFim, profundidade)
            profundidade += 1

        mostrarCaminho(arvore, self.grafo_inga, "Aprofundamento Iterativo")
