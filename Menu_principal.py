
from principal_class import Tree
from datos_tree import tree_size, tree_height, tree_leaves, tree_for_level
import grafico as graf


Arbol = Tree()

def regresar_menu(menu):
    menu = False
    
    print("¿Desea realizar otra operación?")
    print("1. Sí")
    print("2. No")

    menu_activo = input("Digite su desición: ")

    if menu_activo == "1": 
        menu = True
        print("-----Regresando al menú principal-----")
    
    if menu_activo == "2":
        print("-----Saliendo del programa-----")
        menu = False

    if menu_activo != "1" and menu_activo != "2":
        print("Operación no válida")
        regresar_menu(menu)
        menu = False
    
    return menu
            

def menu_principal():
    
    menu = True
    
    while menu:
        print("ARBOLES AVL")
        print("---Bienvenidos a la implementación de árboles AVL---")
        print("¿Qué operación desea realizar?")
        print("1. Insertar un nodo")
        print("2. Eliminar un nodo")
        print("3. Búsqueda de nodos")
        print("4. Mostrar el árbol")
        print("5. Salir")

        menu_section = input("Ingrese el número de la operación que desea realizar: ")

        if menu_section == "1":
            print("------------------------Insertar un nodo------------------------")
            elem = input("Escribe el nombre del archivo a ingresar sin su extención (Ejemplo: '0001')")
            elem = elem.lower()
            if graf.Search_image(elem)!= None:
                if Arbol.get_root() == None:
                    Arbol.set_root(elem)
                else:
                    Arbol.insert(elem)
                print('Inserción exitosa')
            else:
                print('Elemento no existe, intente con otro nombre de archivo')
            print("------------------------Mostrar el árbol------------------------")
            menu = regresar_menu(menu)
            
        if menu_section == "2":
            print("------------------------Eliminar un nodo------------------------")
            print("------------------------Mostrar el árbol------------------------")
            menu = regresar_menu(menu)
            
        if menu_section == "3":
            print("1.Buscar un nodo por nombre de archivo")
            print("2.Buscar nodos por tipo y peso de archivo")
            
            tipo_busqueda = input("Ingrese el número de la operación que desea realizar: ")
            
            if tipo_busqueda == "1":
                busqueda = input("Escriba el nombre del archivo asociado al nodo: ")
                print("------------------------Buscar un nodo por nombre de archivo------------------------")
                menu = regresar_menu(menu)
                
            if tipo_busqueda == "2":
                print("1.Buscar nodos por tipo")
                print("2.Buscar nodos peso")
                print("3.Buscar nodos por peso y tipo")
                tipo_busqueda2 = input('Digita la operación a realizar: ')
                
                if(tipo_busqueda2 == "1" or tipo_busqueda2 == "3"):
                    print("Escriba el tipo de archivo que desea buscar", "/n", "(Las categorias permitidas son: Bike, Cars, Cats, Dogs, Flowers, Horses y Human)")
                    busqueda = input("Categoria: ")
                    
                if(tipo_busqueda2 == "2" or tipo_busqueda2 == "3"):
                    print("Escriba el valor del peso minimo y maximo del archivo en Bytes que desea buscar: ")
                    peso_min = input("Valor de peso Minimo: ")
                    peso_max = input("Valor de peso Maximo: ")
                    
                elif tipo_busqueda2 != "1" or tipo_busqueda2 != "2" or tipo_busqueda2 != "2":
                    print("Operación no válida")
                
                print("------------------------Buscar nodos por tipo y peso de archivo------------------------")
                menu = regresar_menu(menu)
                
            elif tipo_busqueda != "1" or tipo_busqueda != "2":
                print("Operación no válida")
                
            #Debo mostrar esta informaciín cada vez que se busque un nodo.
            nivel_nodo = 0 
            factor_equilibrio_nodo = 0
            pad_nodo = 0
            abu_nodo = 0
            tio_nodo = 0
            
            menu = regresar_menu(menu)
            
        if menu_section == "4": 
            print("------------------------Mostrar el árbol------------------------")
            menu = regresar_menu(menu)
            
        if menu_section == "5":             
            print("-----Saliendo del programa-----")
            menu = False
            
        if menu_section != "1" and menu_section != "2" and menu_section != "3" and menu_section != "4" and menu_section != "5": 
            print("Operación seleccionada no válida")
            menu = regresar_menu(menu)
            
    print("-----Gracias por utilizar el programa------")
    print("-----Hasta luego-----")