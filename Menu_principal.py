from principal_class import Tree, Node
from graph_list import GraphList

#Función para regresar al menú principal
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

#Función para el menú principal
def menu_principal():
    
    #Mensajes de introduccion al programa
    print("----- Bienvenido al programa de creacion de arboles AVL -----")
    print("----- Cargando datos de la carpeta Data -----")
    elem_root = input("Ingrese el nombre del archivo para establecer la raiz del arbol, sin su extención (Ejemplo: '0001'): ")
    
    #Creación del árbol
    Arbol = Tree(Node(elem_root))
    '''
    #Creación del gráfico
    grafico = Grafico()
    grafico.insert_imagen_nodo(Arbol.get_root().get_data())
    '''
    
    #Inicializar vector con los nodos de busqueda
    nodos_consultados = []
    
    menu = True
    
    while menu:
        
        print("ALBOL AVL CREADO SATISFACTORIAMENTE")
        print("----- Bienvenidos a las operaciones de árboles AVL -----")
        print("¿Qué operación desea realizar?")
        print("1. Insertar un nodo")
        print("2. Eliminar un nodo")
        print("3. Búsqueda de nodos")
        print("4. Consultar los nodos buscados")
        print("5. Recorrido por niveles")
        print("6. Mostrar el árbol")
        print("7. Salir")

        menu_section = input("Ingrese el número de la operación que desea realizar: ")

        if menu_section == "1":
            print("------------------------ Insertar un nodo ------------------------")
            elem = input("Escribe el nombre del archivo a ingresar sin su extención (Ejemplo: '0001'): ")
            elem = elem.lower()
            if GraphList.Search_image(GraphList, elem) != None:
                if Arbol.insert(elem):
                    print('Inserción exitosa')
                    print("------------------------ Arbol creado en la carpeta test-grafico-generado ------------------------")
                    Arbol.get_list_ady().plot(Arbol.levels_nr())
                else:
                    print('El elemento ya existe en el arbol. :)')
            else:
                print('Elemento no existe, intente con otro nombre de archivo')
            
            menu = regresar_menu(menu)
            
        if menu_section == "2":
            print("------------------------ Eliminar un nodo ------------------------")
            elem = input("Escribe el nombre del archivo a eliminar sin su extención (Ejemplo: '0001'): ")
            elem = elem.lower()
            if GraphList.Search_image(GraphList, elem) != None:
                if Arbol.delete(elem):
                    print('Eliminación exitosa')
                    print("------------------------ Arbol mostrado en la carpeta test-grafico-generado ------------------------")
                    Arbol.get_list_ady().plot(Arbol.levels_nr())
                else:
                    print('El elemento no existe en el arbol. :)')
            else:
                print('Elemento no existe, intente con otro nombre de archivo')
            menu = regresar_menu(menu)
            
        if menu_section == "3":
            
            print("1.Buscar un nodo por nombre de archivo")
            print("2.Buscar nodos por tipo y peso de archivo")
            
            tipo_busqueda = str(input("Ingrese el número de la operación que desea realizar: "))
            
            if tipo_busqueda == "1":
                print("------------------------ Buscar un nodo por nombre de archivo ------------------------")
                busqueda = input("Escriba el nombre del archivo asociado al nodo, sin su extención (Ejemplo: '0001'): ")
                busqueda = busqueda.lower()
                if GraphList.Search_image(GraphList, busqueda) != None:
                    p, pad = Arbol.search(busqueda)
                    if(p != None):
                        nodos_consultados.append(p.get_data())
                        print('<<<<<<<<<<<<< - Nodo Encontrado, agregado a la lista de nodos consultados - >>>>>>>>>>>>')
                    else:
                        print('Algun nodo con ese archivo no se ha creado, intente con otro nombre de archivo')

                menu = regresar_menu(menu)
                
            if tipo_busqueda == "2":
                
                print("1.Buscar nodos por tipo")
                print("2.Buscar nodos por peso")
                print("3.Buscar nodos por peso y tipo")
                tipo_busqueda2 = str(input('Digita la operación a realizar: '))
                
                if(tipo_busqueda2 == "1"):
                    print("------------------------ Buscar nodos por tipo de archivo ------------------------")
                    print("Escriba el tipo de archivo que desea buscar", "\n", "(Las categorias permitidas son: Bike, Cars, Cats, Dogs, Flowers, Horses y Human)")
                    busqueda = str(input("Categoria: "))
                    busqueda = busqueda.lower()
                    if (busqueda != "bike" and busqueda != "cars" and busqueda != "cats" and busqueda != "dogs" and busqueda != "flowers" and busqueda != "horses" and busqueda != "human"):
                        print("Operación no válida")
                    else:
                        List_nodes_types = Arbol.nodes_type(busqueda)

                        print("Buscando nodos...")
                        if len(List_nodes_types) == 0:
                            print("No se encontraron nodos que cumplan con la condición")
                        else:
                            print(" <<<<<<<<<<<<< - Los nodos que cumplen con la condicion de busqueda: - >>>>>>>>>>>>")
                            for node in List_nodes_types:
                                nodos_consultados.append(node)
                                print(node)
                    
                if(tipo_busqueda2 == "2"):
                    
                    print("------------------------ Buscar nodos por peso de archivo ------------------------")
                        
                    print("Escriba el valor del peso minimo y maximo del archivo en Bytes que desea buscar: ")
                    peso_min = int(input("Valor de peso Minimo: "))
                    peso_max = int(input("Valor de peso Maximo: "))
                    
                    if(peso_min > peso_max):
                        print("Operación no válida")
                    else:
                        print("Buscando nodos...")
                        List_nodes_sizes = Arbol.nodes_sizes(peso_min, peso_max)
                        if len(List_nodes_sizes) == 0:
                            print("No se encontraron nodos que cumplan con la condición")
                        else:
                            print("<<<<<<<<<<<<< - Los nodos que cumplen con la condicion de busqueda: - >>>>>>>>>>>>")
                            for node in List_nodes_sizes:
                                nodos_consultados.append(node)
                                print(node)

                if(tipo_busqueda2 == "3"):
                    flag_type = False
                    flag_size = False
                    
                    print("------------------------ Buscar nodos por peso y tipo de archivo ------------------------")
                    print("Escriba el tipo de archivo que desea buscar", "\n", "(Las categorias permitidas son: Bike, Cars, Cats, Dogs, Flowers, Horses y Human)")
                    busqueda = str(input("Categoria: "))
                    
                    print("Escriba el valor del peso minimo y maximo del archivo en Bytes que desea buscar: ")
                    peso_min = int(input("Valor de peso Minimo: "))
                    peso_max = int(input("Valor de peso Maximo: "))
                    
                    busqueda = busqueda.lower()
                    if (busqueda != "bike" and busqueda != "cars" and busqueda != "cats" and busqueda != "dogs" and busqueda != "flowers" and busqueda != "horses" and busqueda != "human"):
                        print("Operación no válida, tipo de archivo no válido")
                    else:
                        List_nodes_types = Arbol.nodes_type(busqueda)
                        if len(List_nodes_types) != 0:
                            flag_type = True
                    
                    if(peso_min > peso_max):
                        print("Operación no válida con respecto a los pesos de archivo, informacion no válida")
                    else:
                        List_nodes_sizes = Arbol.nodes_sizes(peso_min, peso_max)
                        if len(List_nodes_sizes) != 0:
                            flag_size = True
                                
                    if(flag_type == False or flag_size == False):
                        print("No se encontraron nodos que cumplan con las dos condición")
                    else:
                        print("Buscando nodos...")
                        same_condition = []
                        for node in List_nodes_types:
                            if node in List_nodes_sizes:
                                same_condition.append(node)

                        if len(same_condition) == 0 :
                            print("No se encontraron nodos que cumplan con las dos condición")
                        else:
                            print(" <<<<<<<<<<<<< - Los nodos que cumplen con ambas condiciones de busqueda - >>>>>>>>>>>> ")
                            for node in same_condition:
                                nodos_consultados.append(node)
                                print(node)
                    
                elif tipo_busqueda2 != "1" and tipo_busqueda2 != "2" and tipo_busqueda2 != "3":
                    print("Operación no válida")
                        
                
                menu = regresar_menu(menu)
                
            elif tipo_busqueda != "1" and tipo_busqueda != "2":
                print("Operación no válida")
            
            menu = regresar_menu(menu)
            
        if menu_section == "4": 
            print("------------------------ Nodos encontrados en la operación 3 ------------------------")
            
            if len(nodos_consultados) == 0:
                print("No se han realizado búsquedas")
            else:
                print("Nodos consultados: ")
                for i in range(len(nodos_consultados)):
                    print([i+1],".",nodos_consultados[i], "/n")

                Consul_info = input("¿De cual nodo quiere ver la información? (Digita el numero correspondiente): ")
                
                if(int(Consul_info) > (len(nodos_consultados)+1)):
                    print("Operación no válida")
                    #menu = regresar_menu(menu)
                    #continue
                else:
                    Consul_info = nodos_consultados[int(Consul_info)-1]
                    print("<<<<<< - Datos del nodo encontrado - >>>>>>")
                    Arbol.node_datas(Consul_info)
            
            menu = regresar_menu(menu)
            
        if menu_section == "5": 
            print("------------------------ Recorrido del Arbol AVL por niveles ------------------------")
            recorrido_niveles = []
            Arbol.levels(recorrido_niveles)
            print ("Recorrido por niveles: ", recorrido_niveles)
            menu = regresar_menu(menu)
            
        if menu_section == "6": 
            print("------------------------ Arbol mostrado en la carpeta test-grafico-generado ------------------------")
            Arbol.get_list_ady().plot(Arbol.levels_nr())
            menu = regresar_menu(menu)
            
        if menu_section == "7":             
            print("----- Saliendo del programa -----")
            menu = False
            
        if menu_section != "1" and menu_section != "2" and menu_section != "3" and menu_section != "4" and menu_section != "5" and menu_section != "6" and menu_section != "7": 
            print("Operación seleccionada no válida")
            menu = regresar_menu(menu)
            
    print("----- Gracias por utilizar el programa ------")
    print("----- Hasta luego -----")