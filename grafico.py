from graphviz import Digraph
import imagesize
from matplotlib.ft2font import FIXED_SIZES
from numpy import size
import os
import principal_class as pc

from PIL import Image


dot = Digraph(comment='Mi Gráfico')

def Search_image(name_file):
    carpeta = 'Data'
    directorio_actual = os.path.abspath(carpeta)
    for imagenes in os.listdir(carpeta):
        path = os.path.join(directorio_actual, imagenes)
        Format = imagenes.split('.')[1]
        imagenes = imagenes.split('.')[0]
        if imagenes == name_file:
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
            else:
                print("Imagen encontrada satisfactoriamente")
                return path

    print("Imagen no encontrada")
    return None

def define_father(self, data_s):
    pass

def insert_imagen_nodo(dot, name_file):
    
    if Search_image(name_file) != None:
        imagen = Search_image(name_file)
        print(imagen)
        name_file = str(os.path.basename(imagen))
        size = str(os.path.getsize(imagen))
        new_node = dot.node(name_file, name_file + '\n' + size + ' bytes', image=imagen, fontsize="7", fontcolor='WHITE', style='filled', border = '2', fixedsize='true', shape='rect', penwidth='4')
        return new_node
    else:
        print("Imagen no encontrada, no se puede insertar en el nodo")
        return None
    

def node_conection(dot, name_file):
    if(insert_imagen_nodo(dot, name_file) != None):
        node = insert_imagen_nodo(dot, name_file)
        dot.edge(node, node, arrowsize='0.5')
        return dot
    else:
        print("No se puede conectar el nodo")
        return False

"""
# Crea un objeto de gráfico dirigido
dot = Digraph(comment='Mi Gráfico')

imagen2 = '/Users/carlosp/Documents/GitHub/Autobalanceo/Data/flowers/0001.png'
imagen3 = '/Users/carlosp/Documents/GitHub/Autobalanceo/Data/bike/bike_001.bmp'

# Ruta a la imagen BMP
bmp_path = "/Users/carlosp/Documents/GitHub/Autobalanceo/Data/bike/bike_001.bmp"
/Users/carlosp/Documents/GitHub/Autobalanceo/Data/0001.png
# Cargar la imagen BMP
imagen_bmp = Image.open(bmp_path)

# Guardar la imagen en formato PNG
png_path = "/Users/carlosp/Documents/GitHub/Autobalanceo/Data/bike/bike_001.png"
imagen_bmp.save(png_path, "PNG")


imagen4 = '/Users/carlosp/Documents/GitHub/Autobalanceo/Data/flowers/0003.png'
imagen5 = '/Users/carlosp/Documents/GitHub/Autobalanceo/Data/horses/horse-191.jpg'
nameimagen5 = str(os.path.basename(imagen5))

# Añade nodos
dot.node('A', ' ', image=imagen2, fixedsize='true', shape='rect', penwidth='4')
dot.node('B', ' ', image=png_path, fixedsize='true', shape='rect', penwidth='4')
dot.node('C', ' ', image=imagen4, fixedsize='true', shape='rect', penwidth='4')
dot.node('D', nameimagen5, image=imagen5, fontsize="8", fontcolor='WHITE', style='filled', border = '2', fixedsize='true', shape='rect', penwidth='4')

dot.edge('A', 'B', arrowsize='0.5')
dot.edge('A', 'C', arrowsize='0.5')
dot.edge('C', 'D', arrowsize='0.5')
dot.edge('C', 'F', arrowsize='0.5')
dot.edge('B', 'G', arrowsize='0.5')
dot.edge('B', 'H', arrowsize='0.5')
dot.edge('D', 'I', arrowsize='0.5')
dot.edge('D', 'J', arrowsize='0.5')
dot.edge('H', 'K', arrowsize='0.5')
dot.edge('H', 'L', arrowsize='0.5')
dot.edge('F', 'N', arrowsize='0.5')
dot.edge('F', 'M', arrowsize='0.5')
dot.edge('G', 'S', arrowsize='0.5')
dot.edge('G', 'P', arrowsize='0.5')
 

def create_nodo(self, elem):
    self.dot.node(str(elem), ' ', image=imagen2, fixedsize='true', shape='rect', penwidth='4')
    
"""

def create_graph():
    
    insert_imagen_nodo(dot,'0001')
    insert_imagen_nodo(dot,'0002')
    insert_imagen_nodo(dot,'0195')
    insert_imagen_nodo(dot,'carsgraz_008')
    insert_imagen_nodo(dot,'bike_247')
    
    dot.render('test-output/mi_grafico', view=True)
