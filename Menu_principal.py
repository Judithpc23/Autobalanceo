
from principal_class import node
from datos_tree import tree_size, tree_height, tree_leaves, tree_for_level

menu = True

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
            print("------------------------Buscar un nodo por nombre de archivo------------------------")
            menu = regresar_menu(menu)
            
        if tipo_busqueda == "2":
            print("------------------------Buscar nodos por tipo y peso de archivo------------------------")
            menu = regresar_menu(menu)
            
        elif tipo_busqueda != "1" or tipo_busqueda != "2":
            print("Operación no válida")
            
        #Debo mostrar esta informaciín cada vez que se busque un nodo.
        nivel_nodo = 0 
        factor_equilibrio_nodo = 0
        pad_nodo = node
        abu_nodo = node
        tio_nodo = node
        
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