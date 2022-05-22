class Colonia:

    nombre="-",
    rutas={}

    def __init__(self, nombre, rutas):
        self.rutas = rutas
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre

    def getCostoPorRuta(self, coloniaDestino):
        return self.rutas[coloniaDestino]

    def getRutas(self):
        return self.rutas

    def crearColonia(colonia):
        nombreCol=colonia.get("nombre")
        rutas = {}
        for col in colonia.get("vecinos"):
            nombre = col["nombre"]
            distancia = col["peso"]
            rutas[nombre] = distancia
        return Colonia(nombreCol, rutas)

    def __str__(self):
        return "\n\nNombre Colonia:"+self.nombre+"\nRutas: "+ str(self.rutas)
    



