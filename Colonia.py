class Colonia:

    __nombre = ""
    __rutas = {}

    def __init__(self, nombre, rutas):
        self.__nombre = nombre
        self.__rutas = rutas

    def getNombre(self):
        return self.__nombre

    def getRutas(self):
        return self.__rutas
    
    def getCostoRuta(self, destino):
        return self.__rutas[destino]

    @staticmethod
    def cargarColonia(colonia):
        rutas = {}
        nombre = colonia["nombre"]
        for colAdj in colonia["adyacentes"]:
            nombreAdj = colAdj["nombre"]
            distancia = colAdj["distancia"]
            rutas[nombreAdj] = distancia
        return Colonia(nombre, rutas)

    def __str__(self):
        return "\nNombre Colonia:"+self.nombre+"\nRutas: "+ str(self.rutas)
    



