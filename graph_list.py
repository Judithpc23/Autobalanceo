import graphviz as gv
from typing import List
from typing import Any
import os
from PIL import Image


class GraphList:
    
    #Constructor
    def __init__(self) -> None:
        self.__n = 0
        self.__L: List[List[Any]] = []

    #obetener el numero de vertices
    def get_L(self):
      return self.__L

    #Creacion de un vertice
    def add_vertex(self, size) -> None:
        for i in range(size):
            self.__L.append([])
            self.__n += 1

    #Creacion de una arista
    def add_edge(self, lista_level: List[Any], vi, vf) -> bool:
        self.__L[lista_level.index(vi)].append(vf)
        return True
  
    #Buscar una imagen por su nombre sin extenxion, retornarndo su ruta de acceso.
    def Search_image(self,name_file: str) -> str:
        carpeta = 'Data'
        directorio_actual = os.path.abspath(carpeta)
        for imagenes in os.listdir(carpeta):
            path = os.path.join(directorio_actual, imagenes)
            imagenes_name = imagenes.split('.')
            if len(imagenes_name) > 2:
                imagenes_name = f'{imagenes_name[0]}.{imagenes_name[1]}'
            else:
                imagenes_name = imagenes_name[0]
            if imagenes_name == name_file:
                Format = imagenes.split('.')[-1]
                if(Format == 'bmp'):
                    bmp_path = path
                    # Cargar la imagen BMP
                    imagen_bmp = Image.open(bmp_path)
                    # Guardar la imagen en formato PNG
                    png_path = path
                    png_path = png_path.replace('bmp', 'png')
                    imagen_bmp.save(png_path, "PNG")
                    os.remove(bmp_path)
                    path = png_path
                    #print("Se encontro una imagen en formato bmp, se ha convertido a png")
                    return path
                elif(Format == 'jpg'):
                    bmp_path = path
                    # Cargar la imagen BMP
                    imagen_bmp = Image.open(bmp_path)
                    # Guardar la imagen en formato PNG
                    png_path = path
                    png_path = png_path.replace('jpg', 'png')
                    imagen_bmp.save(png_path, "PNG")
                    os.remove(bmp_path)
                    path = png_path
                    #print("Se encontro una imagen en formato bmp, se ha convertido a png")
                    return path
                else:
                    return path
        return None
        

    #Genera el arbol a partir de una lista de adyacencia.
    def plot(self, lista_level) -> "gv.Digraph":
        graph = gv.Digraph()
        
        #Definir los nodos del grafo
        
        for i in range(self.__n):
            if self.Search_image(f'{lista_level[i]}') != None:
                imagen = self.Search_image(f'{lista_level[i]}')
                name_file = str(os.path.basename(imagen))
                size = str(os.path.getsize(imagen))
                graph.node(f'{lista_level[i]}', f'{name_file}\n{size} bytes', image=imagen, fontsize="7", fontcolor='WHITE', style='filled', border = '2', fixedsize='true', shape='rect', penwidth='4')
            #else:
                #graph.node(f'{lista_level[i]}' , f'{lista_level[i]}', fontsize="7", fontcolor='WHITE', style='filled', border = '2', fixedsize='true', shape='rect', penwidth='4')

        #Lista para las aristas, para no repetir aristas
        edges = []

        # ZIP --> Para agrupar pares por cada posicion
        for l, i in zip(self.__L, range(self.__n)):
            #
            for j in l:
                if not ((i, j) in edges or (j, i) in edges):
                    graph.edge(f'{lista_level[i]}', f'{j}', arrowsize='0.5')
                    #Añado a la lista
                    edges.append((i, j))
        #return graph.render(f'test-grafico-generado/mi_grafico{random.randint(0,50)}',format='pdf', view=True, cleanup=True)
        return graph.render('test-grafico-generado/mi_grafico',format='pdf', view=True, cleanup=True)