class Ciudad:

    nombre="-"
    colonias=[]

    def __init__(self, nombre):
        self.nombre = nombre

    def agregarColonia(self, colonia):
        self.colonias.append(colonia)

    def getNombre(self):
        return self.nombre
    
    def getColonias(self):
        return self.colonias

    def agregarColonia(self, colonia):
        self.colonias.append(colonia)

    def __str__(self):
        return "Nombre ciudad: "+self.nombre+" ".join(map(str,self.colonias))
        
        
