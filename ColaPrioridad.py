import queue


class ColaPrioridad:    

    def __init__(self):
        self.queue = []        

    def estaVacia(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def insertar(self, nodoInsertar):
        costoNodo = nodoInsertar.getCostoCamino()
        indice = 0
        for nodo in self.queue:
            if nodo.getCostoCamino() <= costoNodo:
                indice+=1
            else:
                break
        if indice == -1:
            self.queue.insert(0,nodoInsertar)
        else:
            self.queue.insert(indice,nodoInsertar)
    
    def pop(self):
        retVal = self.queue[0]
        del self.queue[0]
        return retVal     

    #Busca si el estado ya esta en la cola.
    def seEncuentra(self, nodoBuscar):
        for i, nodo in enumerate(self.queue):
            if nodoBuscar.getEstado() == nodo.getEstado():
                return i
        return -1

    #Intercambio por funcion de costo (el menor)
    def intercambiarMejorEstado(self, nodoComparar, indice):
        nodoActual = self.queue[indice]
        if nodoActual.getCostoCamino() > nodoComparar.getCostoCamino():
            del self.queue[indice]
            self.insertar(nodoComparar)
    

