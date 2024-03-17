import random
import graphviz as gv
from typing import List
from typing import Any

class GraphList:
    def __init__(self) -> None:
        self.__n = 0
        self.__L: List[List[Any]] = []

    def get_L(self):
      return self.__L

    def add_vertex(self, size) -> None:
        for i in range(size):
            self.__L.append([])
            self.__n += 1

    def add_edge(self, lista_level: List[Any], vi, vf) -> bool:
      self.__L[lista_level.index(vi)].append(vf)
      return True

    def plot(self, lista_level) -> "gv.Graph":
        graph = gv.Graph()
        #Definir los nodos del grafo
        for i in range(self.__n):
            graph.node(f'{lista_level[i]}', f'{lista_level[i]}')

        #Lista para las aristas, para no repetir aristas
        edges = []

        # ZIP --> Para agrupar pares por cada posicion
        for l, i in zip(self.__L, range(self.__n)):
            #
            for j in l:
                if not ((i, j) in edges or (j, i) in edges):
                    graph.edge(f'{lista_level[i]}', f'{j}')
                    #Añado a la lista
                    edges.append((i, j))
        return graph.render(f'test-grafico-generado/mi_grafico{random.randint(0,50)}',format='png', view=False)