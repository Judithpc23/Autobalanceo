import graphviz as gv

from pprint import pprint
from queue import Queue
from typing import List

class GraphList:
    def __init__(self) -> None:
        self.__n = 0
        self.__L: List[List[int]] = []
    
    def add_vertex(self, height) -> None:
        for i in range(height):
            self.__L.append([])
            self.__n =+ 1

    def add_edge(self, vi: int, vf: int) -> bool:
        if not ((0 <= vi < self.__n) and (0 <= vf < self.__n)):
            return False
        self.__L[vi].append(vf)
        self.__L[vf].append(vi)
        return True

    def plot(self) -> "gv.Graph":
        graph = gv.Graph()
        #Definir los nodos del grafo
        for i in range(self.__n):
            graph.node(f'{i}', f'{i}')

        #Lista para las aristas, para no repetir aristas
        edges = []

        # ZIP --> Para agrupar pares por cada posicion
        for l, i in zip(self.__L, range(self.__n)):
            #
            for j in l:
                if not ((i, j) in edges or (j, i) in edges):
                    graph.edge(f'{i}', f'{j}')
                    #Añado a la lista
                    edges.append((i, j))
        return graph
