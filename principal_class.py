from lib2to3.pytree import type_repr
from queue import Queue
from typing import Any, List, Optional, Tuple
from xmlrpc.client import Boolean

from sympy import nextprime, root
import grafico as gf

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



class Tree:

    def __init__(self) -> None:
        self.__root = None
    
    def set_root(self, root):
        self.__root = root
    
    def get_root(self):
        return self.__root

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
    
    def search_father(self, data_s: Any) -> None:
        p, pad = self.__root, None
        s, flag = [], False
        while (p is not None or len(s) != 0) and not flag:
            if p is not None:
                if p.get_data() == data_s:
                    if pad is not None:
                        print(f'El padre de {data_s!r} es {pad.get_data()!r}')
                    flag = True
                else:
                    s.append(p)
                    pad = p
                    p = p.get_left()
            else:
                p = s.remove()
                pad = p
                p = p.get_right()

        if not flag or pad is None:
            print(f'Para {data_s!r} no hay padre')
    
    def get_height(self, node: "Node"):
        if node is None:
            return 0
        else:
            return max(self.get_height(node.get_left()), self.get_height(node.get_right())) + 1
    
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
        
    def insert(self, elem) -> bool:
        root = self.get_root()
        to_insert = Node(elem)
        if root == None:
            root = to_insert
            return True
        else:
            p, pad = self.search(elem)
            if p != None:
                return False
            elif elem < pad.get_data():
                pad.set_node_left(to_insert)
            else:
                pad.set_node_right(to_insert)
            return True
        
    def pred (self, node: 'Node'):
        p, pad = node.get_left(), None
        while p.get_right() is not None:
            pad = p
            p = p.get_right()
        return p, pad

    
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
            
            return True
        return False