class Colonia:

    nombre = ""
    rutas = {}

    def __init__(self, nombre, rutas):
        self.nombre = nombre
        self.rutas = rutas

    def getNombre(self):
        return self.nombre

    def getRutas(self):
        return self.rutas
    
    def getCostoRuta(self, destino):
        return self.rutas[destino]

    def cargarColonia(colonia):
        rutas = {}
        nombre = colonia["nombre"]
        for colAdj in colonia["vecinos"]:
            distancia = colAdj["distancia"]
            nombreAdj = colAdj["nombre"]
            rutas[nombreAdj] = distancia
        return Colonia(nombre, rutas)


    def __str__(self):
        return "\nNombre Colonia:"+self.nombre+"\nRutas: "+ str(self.rutas)
    



