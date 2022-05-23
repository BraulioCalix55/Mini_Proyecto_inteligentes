class Nodo:

    estado = None
    padre = None
    accion = None
    costoCamino = 0

    def __init__(self, estado, padre, accion, costoCamino):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costoCamino = costoCamino    

    def getCostoCamino(self):
        return self.costoCamino

    def getEstado(self):
        return self.estado
    
    def getAccion(self):
        return self.accion

    def getPadre(self):
        return self.padre

    #función recursiva que calcula el costo de una ruta (Especial A*) y agrega a la lista enviada las acciones de la ruta encontrada
    def rutaEncontrada(self, ciudad, recorrido):
        if self.padre != None:
            lugarA = self.padre.getEstado().getNombreColoniaEstado()
            lugarB = self.estado.getNombreColoniaEstado()
            coloniaA = ciudad.getColonia(lugarA)
            recorrido.append(self.accion)
            return coloniaA.getCostoRuta(lugarB) + self.padre.rutaEncontrada(ciudad, recorrido)  
        else:
            return 0    