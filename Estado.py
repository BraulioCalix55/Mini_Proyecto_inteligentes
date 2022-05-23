class Estado():
    
    coloniaEstado = None
    listaColoniasFaltantes = []
    
    def __init__(self, coloniaEstado, listaColoniasFaltantes):
        self.coloniaEstado = coloniaEstado
        self.listaColoniasFaltantes = listaColoniasFaltantes
    
    def getColoniaEstado(self):
        return self.coloniaEstado

    def getNombreColoniaEstado(self):
        return self.coloniaEstado.getNombre()
    
    def getColoniasFaltantes(self):
        return self.listaColoniasFaltantes  
    
   #Funcion que elimina la colonia donde ya se hizo una entrega, y reacomoda la lista con las colonias pendientes.
    def nuevasColoniasFaltantes(self, coloniaRemover):
        nuevaLista = []
        for colonia in self.listaColoniasFaltantes:
            if coloniaRemover != colonia:
                nuevaLista.append(colonia)
        return nuevaLista
    
    #Retorna si la colonias que se esta visitando es la colonia de destino, y si no hay colonias pendientes por visitar
    def esDestino(self, destino):
        if (self.coloniaEstado.getNombre() == destino) and (len(self.listaColoniasFaltantes) == 0):
            return True
        return False
  