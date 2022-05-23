from Colonia import Colonia
from ColaPrioridad import ColaPrioridad
from Ciudad import Ciudad
from Nodo import Nodo
from Estado import Estado
import json
from queue import Queue


class Busqueda:

    coloniaInicial = ""
    lugaresEntregas = []
    costoMaximo = 0.0
    ciudad = None

    def __init__(self, coloniaInicial, lugaresEntregas, costoMaximo):
        self.coloniaInicial = coloniaInicial
        self.lugaresEntregas = lugaresEntregas
        self.costoMaximo = costoMaximo

    def cargarMapa(self, nombreArchivo):
        myJsonFile = open(nombreArchivo, 'r')
        jsonData = myJsonFile.read()
        obj = json.loads(jsonData)
        listaColonias = obj['colonias']
        self.ciudad = Ciudad(obj["ciudad"])
        for i in range(len(listaColonias)):
            self.ciudad.addColonia(Colonia.cargarColonia(listaColonias[i]))


    def costoUniforme(self):
        nodo = self.nodoInicial(True)
        frontera = ColaPrioridad()
        frontera.insertar(nodo)
        explorados = set()
        while True:
            if frontera.estaVacia():
                print("No se encuentra niguna ruta disponible")
                return
            nodo = frontera.pop()
            #Se evalua si el nodo actual es la ruta a donde se quiere llegar
            if nodo.getEstado().esDestino(self.coloniaInicial):
                self.solucion(nodo)
                print("Nodos explorados: ", len(explorados))
                print("Nodos totales:  ",
                      len(explorados) + frontera.size())
                return
            explorados.add(nodo.getEstado())
            coloniaActual = nodo.getEstado().getColoniaEstado()
            #Las acciones validas son las colinias vecinas dentro de cada colonia
            for ruta in coloniaActual.getRutas().keys():
                nodoHijo = self.hacerNodoHijo(
                    nodo, ruta, coloniaActual.getRutas()[ruta], True)
                seEncuentraFrontera = frontera.seEncuentra(nodoHijo)

                if (not self.enExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    frontera.insertar(nodoHijo)
                elif seEncuentraFrontera != -1:
                    frontera.intercambiarMejorEstado(
                        nodoHijo, seEncuentraFrontera)

    def BFS(self):
        frontera = Queue()
        explorados = set()
        nodo = self.nodoInicial(True)
        frontera.put(nodo)
        cont = 1
        while True:
            cont += 1
            if frontera.empty():
                print("No hay ruta disponible\n")
                return
            listaVacia = len(nodo.getEstado().getColoniasFaltantes()) #Verifica si hay colonias que falta por visitar
            if nodo.getEstado().esDestino(self.coloniaInicial) and listaVacia == 0:
                self.solucion(nodo)
                print("Total de nodos explorados:", len(explorados))
                print("Total de nodos descubiertos:",
                      len(explorados) + frontera.qsize())
                return
            nodo = frontera.get()  #Obtener el primer elemento de la cola
            explorados.add(nodo.getEstado())  #Se agrega el nodo a la lista de explorados. 
            colActual = nodo.getEstado().getColoniaEstado()
            adyacentes = colActual.getRutas().keys()
            for v in adyacentes:
                nodoHijo = self.hacerNodoHijo(nodo, v, colActual.getRutas()[v], True)
                seEncuentraFrontera = False
                for elem in list(frontera.queue):
                    if nodoHijo == elem:
                        seEncuentraFrontera = True
                if (not self.enExplorados(explorados, nodoHijo.getEstado())) or (seEncuentraFrontera == -1):
                    explorados.add(nodoHijo.getEstado())
                    frontera.put(nodoHijo)

    '''Creacion del nodo inicial, tomando en cuenta el Estado, que toma la colonia inicial y 
    hacia donde se puede mover, padre al que pertenece el nodo (se toma vacio puesto que es el nodo inicial),
    acciones disponibles (donde se muestra el resultado de la ruta) y  el costo que tiene el camino (inicial en cero)'''

    def nodoInicial(self, esCostoUniforme):
        coloniaInicial = self.ciudad.getColonia(self.coloniaInicial)
        if esCostoUniforme:
            return Nodo(Estado(coloniaInicial, self.lugaresEntregas), None, "Inicio -> "+self.coloniaInicial, 0)
        else:
            return Nodo(Estado(coloniaInicial, self.lugaresEntregas), None, "Inicio -> "+self.coloniaInicial, len(self.lugaresEntregas))
  
    #Crea el nuevo nodo a partir de la información del padre, con sus respectivas rutas, y es adjuntado al padre.
    def hacerNodoHijo(self, padre, ruta, costoRuta, esCostoUniforme):
        Colonia = self.ciudad.getColonia(ruta)
        colFaltantes = padre.getEstado().nuevasColoniasFaltantes(ruta)
        if esCostoUniforme:
            nuevoCosto = padre.getCostoCamino() + costoRuta
        else:
            nuevoCosto = padre.getCostoCamino() + costoRuta + len(colFaltantes)
        nuevaAccion = padre.getEstado().getNombreColoniaEstado() + " hacia " + ruta
        return Nodo(Estado(Colonia, colFaltantes), padre, nuevaAccion, nuevoCosto)

    # Función que busca si el nodo está en los nodos que ya fueron visitados previamente. 
    def enExplorados(self, explorados, estadoBuscar):
        for estado in explorados:
            if estado == estadoBuscar:
                return True
        return False

    #Si se encuentra una ruta dentro del costo esperado, se imprime los destinos a los cuales llego
    def solucion(self, nodo):
        recorrido = []
        costo = nodo.rutaEncontrada(self.ciudad, recorrido)
        if costo > self.costoMaximo:
            print("Hay una ruta de mayor costo que el esperado. ")
            print("Costo encontrado: ", nodo.getCostoCamino())
            print("Costo esperado: ", self.costoMaximo)
        else:
            #El recorrido de los nodos se hace al reves, puesto que el estado meta queda encima de la lista.
            recorrido.reverse()
            print("Ruta:\n")
            for ruta in recorrido:
                print(ruta)
            print("Costo del Recorrido: ",costo)