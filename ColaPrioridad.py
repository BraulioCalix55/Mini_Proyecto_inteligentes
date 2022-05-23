import queue


class ColaPrioridad:    

    def __init__(self):
        self.__queue = []        

    def estaVacia(self):
        return len(self.__queue) == 0

    def insertar(self, nodoInsertar):
        costoNodo = nodoInsertar.getCostoCamino()
        indice = 0
        for nodo in self.__queue:
            if nodo.getCostoCamino() <= costoNodo:
                indice+=1
            else:
                break
        if indice == -1:
            self.__queue.insert(0,nodoInsertar)
        else:
            self.__queue.insert(indice,nodoInsertar)
    
    def pop(self):
        retVal = self.__queue[0]
        del self.__queue[0]
        return retVal     

    #función que busca si un estado ya se encuentra dentro de la priority queue y retorna el indice
    def seEncuentra(self, nodoBuscar):
        for i, nodo in enumerate(self.__queue):
            if nodoBuscar.getEstado() == nodo.getEstado():
                return i
        return -1

    #función que intercambia el nodo, si el nodo recibido tiene un menor costo
    def intercambiarMejorEstado(self, nodoComparar, indice):
        nodoActual = self.__queue[indice]
        if nodoActual.getCostoCamino() > nodoComparar.getCostoCamino():
            del self.__queue[indice]
            self.insertar(nodoComparar)
    
    #función que retorna el size de la priority queue
    def size(self):
        return len(self.__queue)
