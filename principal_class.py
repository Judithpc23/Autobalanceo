from typing import Any, List, Optional, Type
import os

from numpy import delete
from graph_list import GraphList

class Queue:
 
    def __init__(self) -> None:
        self.queue: List['Node'] = []
 
    def put(self, elem: Any) -> None:
        self.queue.append(elem)
 
    def get(self) -> Any:
        return self.queue.pop(0)
 
    def empty(self) -> bool:
        return len(self.queue) == 0

class Node:

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__left: Optional["Node"] = None
        self.__right: Optional["Node"] = None

    def get_data(self):
        return self.__data
    
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_node_left(self, node):
        self.__left = node
    
    def set_node_right(self, node):
        self.__right = node
    
    def set_data(self, data):
        self.__data = data

    def set_type(self, name:str) -> None:
        type = None
        
        if(name.split()[0]== '0'):
            type = 'Flower'
        elif(name.split('-')[0] == 'carsgraz'):
            type = 'Car'
        elif(name.split('.')[0] == 'cat'):
            type = 'Cat'
        elif(name.split('-')[0] == 'rider'):
            type = 'Human'
        elif(name.split('.')[0] == 'dog'):
            type = 'Dog'
        elif(name.split('-')[0] == 'horse'):
            type = 'Horse'
        elif(name.split('.')[0] == 'bike'):
            type = 'Bike'
        
        return type
    
    def set_size(self, name:str) -> None:
        
        size = None
        
        imagen = self.Search_image(name)
        name = str(os.path.basename(imagen))
        size = str(os.path.getsize(name))
        
        return size



class Tree:

    def __init__(self, root: 'Node') -> None:
        self.__root = root
        self.__list_ady: Optional['GraphList'] = [[]]

        self.set_list_ady()
        
    def set_root(self, root):
        self.__root = root
        # gf.Grafico().insert_imagen_nodo(root.get_data())
    
    def get_root(self):
        return self.__root
    
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

    #Obtener lista de adyacencia del árbol
    def get_list_ady(self):
        return self.__list_ady
    
    
    # <<<<<<<<<<<<<<<<<< FUNCIONES DE BUSQUEDA, INSERCIÓN Y ELIMINACIÓN >>>>>>>>>>>>>>>>>>>>>>>>

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
    
    #Tamaño del árbol.
    def get_size(self, node:'Node'):
      if node is None:
        return 0
      else:
        return self.get_size(node.get_left()) + 1 + self.get_size(node.get_right())

    def pred (self, node: 'Node'):
        p, pad = node.get_left(), None
        while p.get_right() is not None:
            pad = p
            p = p.get_right()
        return p, pad
    
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
        pad, grandPa = self.search(pad.get_data())
        return grandPa
    
    #Busqueda del tío de un nodo.
    def searchUncle(self, elem: str) -> Optional['bool']:
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
                print(node.data, end=' ')
            self.list_level(node.get_left(), n-1)
            self.list_level(node.get_right(), n-1)
    
    def __levels_r(self, node, level) -> None:
        if level <= self.get_height(self.__root) - 1:
            self.list_level(node, level)
            self.__levels_r(node, level + 1)
    
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
    
    def node_datas(self, node: "Node"):
        
        nivel_nodo = self.get_height()
        factor_equilibrio_nodo = 0
        pad_nodo = self.search_father_node()
        abu_nodo = 0
        tio_nodo = 0
        
        print("Nivel del nodo: ", nivel_nodo)
        print("Factor de equilibrio del nodo: ", factor_equilibrio_nodo)
        print("Padre del nodo: ", pad_nodo)
        print("Abuelo del nodo: ", abu_nodo)
        print("Tio del nodo: ", tio_nodo)
        
    def nodes_sizes(self, min: int, max: int) -> List:
        nodes = []
        nodo = self.get_root()
        queue = Queue()
        queue.put(nodo)
        while not queue.empty():
            nodo = queue.get()
            if nodo.get_data() >= min and nodo.get_data() <= max:
                nodes.append(nodo.get_data())
            if nodo.get_left() != None:
                queue.put(nodo.get_left())
            if nodo.get_right() != None:
                queue.put(nodo.get_right())
        return nodes
    
    def nodes_type(self, category: str) -> List:
        categoria = []
        nodo = self.get_root()
        queue = Queue()
        queue.put(nodo)
        while not queue.empty():
            nodo = queue.get()
            node_data = nodo.get_data()
            if nodo.set_type(node_data) == category:
                categoria.append(node_data)
            if nodo.get_left() != None:
                queue.put(nodo.get_left())
            if nodo.get_right() != None:
                queue.put(nodo.get_right())
        return categoria


T = Tree(Node(7))
T.insert(4)
T.insert(54)
T.insert(40)
T.insert(60)
T.insert(3)
print(T.insert(5))
print(T.searchGrandPa(40).get_data())
print(T.searchUncle(40).get_data())

T.get_list_ady().plot(T.levels_nr())

print(T.levels_nr())
T.delete(60)

print(T.levels_nr())
print(T.get_list_ady().get_L())
T.get_list_ady().plot(T.levels_nr())