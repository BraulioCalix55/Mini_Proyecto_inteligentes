from msilib.schema import Class


class Nodo:
    def __init__(self,nombre,pesos,vecinos):
        self.nombre=nombre
        self.pesos=pesos
        self.vecinos=vecinos
    def imprimir(self):
        print(self.nombre , self.peso , self.vecinos)
        