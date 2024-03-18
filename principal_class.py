from typing import Any, List, Optional, Type
import os
from graph_list import GraphList

class Queue:
    
    #Constructor de la clase.
    def __init__(self) -> None:
        self.queue: List['Node'] = []
    
    #Agregar un elemento a la cola.
    def put(self, elem: Any) -> None:
        self.queue.append(elem)
    
    #Obtener un elemento de la cola.
    def get(self) -> Any:
        return self.queue.pop(0)
 
    #Verificar si la cola está vacía.
    def empty(self) -> bool:
        return len(self.queue) == 0
    
class Stack:
    
    #Constructor de la clase.
    def __init__(self) -> None:
        self.stack: List[Any] = []

    #Agregar un elemento a la pila.
    def add(self, elem: Any) -> None:
        self.stack.append(elem)

    #Obtener un elemento de la pila.
    def remove(self) -> Any:
        return self.stack.pop()

    #Verificar si la pila está vacía.
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    

class Node:

    #Constructor de la clase.
    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__left: Optional["Node"] = None
        self.__right: Optional["Node"] = None

    #Obtener el dato del nodo.
    def get_data(self):
        return self.__data
    
    #Obtener el nodo izquierdo.
    def get_left(self):
        return self.__left
    
    #Obtener el nodo derecho.
    def get_right(self):
        return self.__right
    
    #Establecer el nodo izquierdo.
    def set_node_left(self, node):
        self.__left = node
    
    #Establecer el nodo derecho.
    def set_node_right(self, node):
        self.__right = node
    
    #Establecer el dato del nodo.
    def set_data(self, data):
        self.__data = data

    #Funcion que me establece el tipo de categoria de la imagen.
    def set_type(self, name:str) -> None:
        type = None
        
        if(name.split()[0]== '0'):
            type = 'flowers'
        elif(name.split('_')[0] == 'carsgraz'):
            type = 'cars'
        elif(name.split('.')[0] == 'cat'):
            type = 'cats'
        elif(name.split('-')[0] == 'rider'):
            type = 'human'
        elif(name.split('.')[0] == 'dog'):
            type = 'dogs'
        elif(name.split('-')[0] == 'horse'):
            type = 'horses'
        elif(name.split('_')[0] == 'bike'):
            type = 'bike'
        
        return type
    
    #Funcion que me establece el tamaño de la imagen del nodo.
    def set_size(self, name:str):
        size = 0
        imagen = GraphList.Search_image(GraphList,name)
        if(imagen != None):
            name_file = str(os.path.basename(imagen))
            size = str(os.path.getsize(imagen))
            if size == 0:
                size = 'No se encontro el tamaño'
            else:
                size = size
        return size


class Tree:

    # <<<<<<<<<<<<<<<<<< INICIALIZAR ARBOL >>>>>>>>>>>>>>>>>>>>>>>>
    
    #Constructor de la clase.
    def __init__(self, root: 'Node') -> None:
        self.__root = root
        self.__list_ady: Optional['GraphList'] = [[]]

        self.set_list_ady()
        
    #Establecer la raíz del árbol.
    def set_root(self, root):
        self.__root = root
    
    #Obtener la raíz del árbol.
    def get_root(self):
        return self.__root
    
    # <<<<<<<<<<<<<<<<<< LISTA DE ADYACENCIA >>>>>>>>>>>>>>>>>>>>>>>>
    
    #Obtener lista de adyacencia.
    def get_list_ady(self):
        return self.__list_ady
        
    #Construir lista de adyacencia.
    def set_list_ady(self):
        self.__list_ady = GraphList()
        self.__list_ady.add_vertex(self.get_size(self.get_root()))
        
        p = self.get_root() 
        q: List['Node'] = []
        q.append(p)
        while not len(q) == 0:
            p = q.pop(0)
            pad = self.search_father(p.get_data())
            if p.get_left() is not None:
                q.append(p.get_left())
            if p.get_right() is not None:
                q.append(p.get_right())
            if p is not None and pad is not None:
              self.__list_ady.add_edge(self.levels_nr(), pad, p.get_data())
    
    # <<<<<<<<<<<<<<<<<< POSTORDEN DEL ARBOL >>>>>>>>>>>>>>>>>>>>>>>>
    
    def postorder_nr(self) -> 'str':
        postorden = ""
        p, s, s_data = self.__root, Stack(), Stack()
        s.add(p)
        while not s.is_empty():
            p = s.remove()
            s_data.add(p.get_data())
            if p.get_left() is not None:
                s.add(p.get_left())
            if p.get_right() is not None:
                s.add(p.get_right())
        while not s_data.is_empty():
            postorden +=f'{s_data.remove()}-'
        return postorden    
    
    # <<<<<<<<<<<<<<<<<< FUNCIONES DE BUSQUEDA, INSERCIÓN Y ELIMINACIÓN >>>>>>>>>>>>>>>>>>>>>>>>

    #Buscar un nodo.
    def search(self, elem):
        p, pad = self.get_root(), None
        while (p != None):
            if p.get_data() == elem:
                return p, pad
            elif elem < p.get_data():
                pad = p
                p = p.get_left()
            else:
                pad = p
                p = p.get_right()
        return p, pad
    
    #Insertar un nodo.
    def insert(self, elem) -> bool:
        root = self.get_root()
        to_insert = Node(elem)
        if root == None:
            root = to_insert
            self.set_list_ady()
            return True
        else:
            p, pad = self.search(elem)
            if p != None:
                return False
            elif elem < pad.get_data():
                pad.set_node_left(to_insert)
            else:
                pad.set_node_right(to_insert)
            self.set_list_ady()
            return True

    #Eliminar un nodo.
    def delete(self, elem) -> bool:
        p, pad = self.search(elem)
        if p != None:
            if p.get_left() == None and p.get_right() == None:
                if p == pad.get_left():
                    pad.set_node_left(None)
                else:
                    pad.set_node_right(None)
            
            elif p.get_left() != None and p.get_right() == None:
                if p == pad.get_left():
                    pad.set_node_left(p.get_left())
                else:
                    pad.set_node_right(p.get_left())
            
            elif p.get_left() == None and p.get_right() != None:
                if p == pad.get_left():
                    pad.set_node_left(p.get_right())
                else:
                    pad.set_node_right(p.get_right())
            
            else:
                pred, pad_pred = self.pred(p) #Algoritmo de predecesor
                p.set_data(pred.get_data())
                if pred.get_left() != None:
                    pad_pred.set_node_right(pred.get_left())
                else:
                    pad_pred.set_node_right(None)
            
            self.set_list_ady()
            return True
        return False
    
    # <<<<<<<<<<<<<<<<<< FUNCIONES DE BUSQUEDA DE PARIENTES >>>>>>>>>>>>>>>>>>>>>>>>
    
    #Busqueda del padre por un dato del nodo.
    def search_father(self, data_s: Any) -> None:
        p, pad = self.__root, None
        s: List["Node"] = [] 
        flag =  False
        while (p is not None or len(s) != 0) and not flag:
            if p is not None:
                if p.get_data() == data_s:
                    if pad is not None:
                        return pad.get_data()
                    flag = True
                else:
                    s.append(p)
                    pad = p
                    p = p.get_left()
            else:
                p = s.pop()
                pad = p
                p = p.get_right()

        if not flag or pad is None:
            return None
            
    #Busqueda del padre por un nodo.
    def search_father_node(self, node: "Node") -> None:
        p, pad = self.__root, None
        s: List["Node"] = []
        flag = False
        while (p is not None or len(s) != 0) and not flag:
            if p is not None:
                if p.get_data() == node.get_data():
                    data_s = node.get_data()
                    if pad is not None:
                        print(f'El padre de {data_s!r} es {pad.get_data()!r}')
                        return pad
                    flag = True
                else:
                    s.append(p)
                    pad = p
                    p = p.get_left()
            else:
                p = s.pop()
                pad = p
                p = p.get_right()

        if not flag or pad is None:
            print(f'Para {data_s!r} no hay padre')
            return None
        
    #Busqueda del abuelo de un nodo.
    def searchGrandPa(self, elem: str):
        p, pad = self.search(elem)
        if pad is not None:
            pad, grandPa = self.search(pad.get_data())
            return grandPa
        return None
    
    #Busqueda del tío de un nodo.
    def searchUncle(self, elem: str) -> Optional['Node']:
        p, pad = self.search(elem)
        grandPa = self.searchGrandPa(elem)
        if grandPa is not None:
          if grandPa.get_left() == pad:
              if grandPa.get_right() is not None:
                  return grandPa.get_right()
          else:
              if grandPa.get_left() is not None:
                  return grandPa.get_left()
        return False
    
    # <<<<<<<<<<<<<<<<<< RECORRIDO POR NIVELES ITERATIVO >>>>>>>>>>>>>>>>>>>>>>>>
    #Recorrido por niveles
    def levels_nr(self) -> None:
        p = self.get_root()
        q: List['Node'] = []
        q.append(p)
        lista = []
        while not len(q) == 0:
            p = q.pop(0)
            lista.append(p.get_data())
            if p.get_left() is not None:
                q.append(p.get_left())
            if p.get_right() is not None:
                q.append(p.get_right())
        return lista

    # <<<<<<<<<<<<<<<<<< RECORRIDO POR NIVELES RECURSIVO >>>>>>>>>>>>>>>>>>>>>>>>
    def get_height(self, node: "Node"):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.get_left()), self.get_height(node.get_right())) + 1

    def list_level(self, node: "Node", n):
        if node != None:
            if n == 0:
                print(node.get_data(), end=' ')
            self.list_level(node.get_left(), n-1)
            self.list_level(node.get_right(), n-1)
    
    def levels_r(self, node, level) -> None:
        if level <= self.get_height(self.__root) - 1:
            self.list_level(node, level)
            self.levels_r(node, level + 1)
    
    def levels(self) -> None:
        self.__levels_r(self.__root, 0)
        
        
    # <<<<<<<<<<<<<<<<<< FUNCIONES PARA EL AUTOBALANCEO >>>>>>>>>>>>>>>>>>>>>>>>
    def get_balance(self, node: "Node"):
        if node is None:
            return 0
        return self.get_height(node.get_right()) - self.get_height(node.get_left())
    
    def rebalance(self, node: "Node"):
        if self.get_balance(node) > 1:
            if self.get_balance(node.get_right()) >= 0:
                pass
                #return self.rotate_left(node)
            else:
                pass
                # return self.rotate_right_left(node)
        elif self.get_balance(node) < -1:
            if self.get_balance(node.get_left()) <= 0:
                pass
                # return self.rotate_right(node)
            else:
                pass
                # return self.rotate_left_right(node)
        return node
        
    # <<<<<<<<<<<<<<<<<< FUNCIONES PARA LA OBTENCIÓN DE DATOS DE LOS NODOS >>>>>>>>>>>>>>>>>>>>>>>>
    
    #Tamaño del árbol.
    def get_size(self, node:'Node'):
      if node is None:
        return 0
      else:
        return self.get_size(node.get_left()) + 1 + self.get_size(node.get_right())

    #Predecesor de un nodo.
    def pred (self, node: 'Node'):
        p, pad = node.get_left(), None
        while p.get_right() is not None:
            pad = p
            p = p.get_right()
        return p, pad
        
    #Buscar un nodo por nivel.
    def node_level(self, elem):
        cont = 0
        p = self.get_root()
        while (p != None):
            if p.get_data() == elem:
                return cont
            elif elem < p.get_data():
                p = p.get_left()
                cont += 1
            else:
                p = p.get_right()
                cont += 1
        return cont
    
    
    #Funcion que me genera el output de la informacion de un nodo.
    def node_datas(self, elem: Any):
        
        node, pad = self.search(elem)
        
        nivel_nodo = self.node_level(elem)
        
        data_size = node.set_size(elem)
        
        factor_equilibrio_nodo = self.get_balance(node)
        if self.search_father(node.get_data()) == None:
            pad_nodo = 'El nodo no tiene padre'
        else:
            pad_nodo = self.search_father(node.get_data())

        if self.searchGrandPa(node.get_data()) == None:
            abu_nodo = 'El nodo no tiene abuelo'
        else:
            abu_nodo = self.searchGrandPa(node.get_data()).get_data()

        if self.searchUncle(node.get_data()) == False:
            tio_nodo = 'El nodo no tiene tío'
        else:
            tio_nodo = self.searchUncle(node.get_data()).get_data()
        print(" ")
        print("Informacion del nodo: ", elem)    
        print("El peso de la imagen: ", data_size, "bytes")
        print(" ")
        print("Nivel del nodo: ", nivel_nodo)
        print("Factor de equilibrio del nodo: ", factor_equilibrio_nodo)
        print("Padre del nodo: ", pad_nodo)
        print("Abuelo del nodo: ", abu_nodo)
        print("Tío del nodo: ", tio_nodo)
        print(" ")
        
        
        
    # <<<<<<<<<<<<<<<<<< FUNCIONES PARA LA OBTENCIÓN DE DATOS DE LOS NODOS >>>>>>>>>>>>>>>>>>>>>>>>
        
    # ----------------- retornar lista de nodos con un rango de peso minimo y maximo -----------------
    def nodes_sizes(self, min: int, max: int) -> List:
        nodes = []
        nodos = self.postorder_nr()
        nodos = nodos.split('-')
        nodos.pop()
        for elem in nodos:
            p, pad = self.search(elem)
            nodo_size = p.set_size(elem)
            if nodo_size >= min and nodo_size <= max:
                nodes.append(p.get_data)
        return nodes
    
    # ----------------- retornar lista de nodos de un mismo tipo de categoria -----------------
    def nodes_type(self, category: str) -> List:
        categoria = []
        nodos = self.postorder_nr()
        nodos = nodos.split('-')
        nodos.pop()
        for elem in nodos:
            p, pad = self.search(elem)
            nodo_category = p.set_type(elem)
            if nodo_category == category:
                categoria.append(p.get_data)
        return categoria


# T = Tree(Node('0001'))
# T.insert('carsgraz_001')
# T.insert('horse-17')
# T.insert('horse-18')
# T.insert('rider-8')
# T.insert('rider-20')
# T.insert('cat.8')
# T.insert('dog.27')
# print(T.insert('bike_128'))
# print(T.searchGrandPa('horse-18').get_data())
# print(T.searchUncle('horse-18').get_data())
# print(T.levels_nr())

# print(T.get_list_ady().get_L())

# print('INFO NODO')
# T.node_datas('rider-8')
# T.get_list_ady().plot(T.levels_nr())