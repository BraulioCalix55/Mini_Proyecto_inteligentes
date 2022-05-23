class Ciudad:
    
    __nombre = ""
    __colonias = []
    
    def __init__(self, nombre):
        self.__nombre = nombre

    def getColonia(self, nombreColonia):
        for colonia in self.__colonias:
            if colonia.getNombre() == nombreColonia:
                return colonia

    def addColonia(self, colonia):
        self.__colonias.append(colonia)
    
    def __str__(self):
        return "Nombre ciudad: "+self.nombre+" ".join(map(str,self.colonias))
        
        
