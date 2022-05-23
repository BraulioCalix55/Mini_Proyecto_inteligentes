class Ciudad:
    
    nombre = ""
    colonias = []
    
    def __init__(self, nombre):
        self.nombre = nombre

    def getColonia(self, nombreColonia):
        for colonia in self.colonias:
            if colonia.getNombre() == nombreColonia:
                return colonia
    
    def getColonias(self):
        return self.colonias

    def addColonia(self, colonia):
        self.colonias.append(colonia)
    
    def __str__(self):
        return "Nombre ciudad: "+self.nombre+" ".join(map(str,self.colonias))  
    
