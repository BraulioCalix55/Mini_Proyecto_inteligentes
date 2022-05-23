class NodoBusqueda:

    __estado = None
    __padre = None
    __accion = None
    __costoCamino = 0

    def __init__(self, estado, padre, accion, costoCamino):
        self.__estado = estado
        self.__padre = padre
        self.__accion = accion
        self.__costoCamino = costoCamino    

    def getCostoCamino(self):
        return self.__costoCamino

    def getEstado(self):
        return self.__estado
    
    def getAccion(self):
        return self.__accion

    def getPadre(self):
        return self.__padre

    #función recursiva que calcula el costo de una ruta (Especial A*) y agrega a la lista enviada las acciones de la ruta encontrada
    def rutaEncontrada(self, ciudad, recorrido):
        if self.__padre != None:
            lugarA = self.__padre.getEstado().getNombreColoniaEstado()
            lugarB = self.__estado.getNombreColoniaEstado()
            coloniaA = ciudad.getColonia(lugarA)
            recorrido.append(self.__accion)
            return coloniaA.getCostoRuta(lugarB) + self.__padre.rutaEncontrada(ciudad, recorrido)  
        else:
            return 0          