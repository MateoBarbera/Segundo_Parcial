#Cargar el esquema de red de la siguiente figura en un grafo e implementar los algsalidatmos
#necesarios para resolver las tareas, listadas a continuación:
#1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
#2. realizar un barrido en profundidad y amplitud partiendo destinode la tres notebook: Red
#Hat, Debian, Arch;
#3. encontrar el camino más corto para enviar a imprimir un documento destinode la pc:
#Debian y Red Hat, hasta el servidor “MongoDB”;
#4. encontrar el árbol de expansión mínima;
#5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#realice un barrido en profundidad para corroborar que efectivamente fue borrada;
#6. debe utilizar un grafo no dirigido.

from TDA_PilaDin import desapilar, pila_vacia
from TDA_Grafo import Grafo,barrido_amplitud_red, barrido_profundidad_red, buscar_vertice_red, dijkstra_red, insertar_arista_red, insertar_vertice_red, marcar_no_visitado,prim_red,eliminar_vertice,barrido_profundidad
from tda_pila import Pila
grafo = Grafo(False)

class Red():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return self.nombre + ' - ' + self.tipo
#carga vertices 
dato = Red('Switch 1', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Switch 2', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Ubuntu', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Mint', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Manjaro', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Fedora', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Parrot', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Debian', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Red Hat', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Arch', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Router 1', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Router 2', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Router 3', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Guaraní', 'Servidor')
insertar_vertice_red(grafo, dato)
dato = Red('MongoDB', 'Servidor')
insertar_vertice_red(grafo, dato)
dato = Red('Impresora', 'Impresora')
insertar_vertice_red(grafo, dato)

#carga aristas
salida = buscar_vertice_red(grafo, 'Switch 1')
destino = buscar_vertice_red(grafo, 'Debian')
insertar_arista_red(grafo, 17, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 1')
destino = buscar_vertice_red(grafo, 'Ubuntu')
insertar_arista_red(grafo, 18, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 1')
destino = buscar_vertice_red(grafo, 'Impresora')
insertar_arista_red(grafo, 22, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 1')
destino = buscar_vertice_red(grafo, 'Mint')
insertar_arista_red(grafo, 80, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 1')
destino = buscar_vertice_red(grafo, 'Router 1')
insertar_arista_red(grafo, 29, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'Manjaro')
insertar_arista_red(grafo, 40, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'Fedora')
insertar_arista_red(grafo, 3, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'Parrot')
insertar_arista_red(grafo, 12, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 61, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'Arch')
insertar_arista_red(grafo, 56, salida, destino)
salida = buscar_vertice_red(grafo, 'Switch 2')
destino = buscar_vertice_red(grafo, 'MongoDB')
insertar_arista_red(grafo, 5, salida, destino)
salida = buscar_vertice_red(grafo, 'Router 1')
destino = buscar_vertice_red(grafo, 'Router 2')
insertar_arista_red(grafo, 37, salida, destino)
salida = buscar_vertice_red(grafo, 'Router 1')
destino = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 43, salida, destino)
salida = buscar_vertice_red(grafo, 'Router 2')
destino = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 50, salida, destino)
salida = buscar_vertice_red(grafo, 'Router 2')
destino = buscar_vertice_red(grafo, 'Guaraní')
insertar_arista_red(grafo, 9, salida, destino)
salida = buscar_vertice_red(grafo, 'Router 2')
destino = buscar_vertice_red(grafo, 'Red Hat')
insertar_arista_red(grafo, 25, salida, destino)

#2. 
notebook = ['Red Hat', 'Debian', 'Arch']
for i in range(len(notebook)):
    print('\nBarrido profundidad:', notebook[i])
    salida = buscar_vertice_red(grafo, notebook[i])
    barrido_profundidad_red(grafo, salida)
    marcar_no_visitado(grafo)

    print('\nBarrido amplitud:', notebook[i])
    salida = buscar_vertice_red(grafo, notebook[i])
    barrido_amplitud_red(grafo, salida)
    marcar_no_visitado(grafo)

#3
print()
dist_min = None
pc = ['Debian', 'Red Hat']
for i in range(len(pc)):
    pila = dijkstra_red(grafo, pc[i], 'MongoDB')
    fin = 'Guaraní'
    distancia = None
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    if dist_min is None:
        dist_min = distancia
        pc_min = pc[i]
    if distancia < dist_min:
        dist_min = distancia
        pc_min = pc[i]

print('PC con menor distancia hasta el servidor MongoDB:', pc_min, '- distancia:', dist_min)
print()
#4
print('Arbol de expansion minima')
bosque = prim_red(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], bosque[i+1])

#5 
clave="Impresora"
eliminar_vertice(grafo, clave)
buscado = "Switch1"
print("Barrido profundidad sin la impresora ") 
origen = buscar_vertice_red(grafo, buscado)
barrido_profundidad_red(grafo, origen)
marcar_no_visitado(grafo)

