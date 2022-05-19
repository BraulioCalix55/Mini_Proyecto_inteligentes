
class Nodo:
    
    estado:None
    accion:None
    padre:None
    costo:0


    def __init__(self,estado,accion,padre,costo):
        self.estado = estado
        self.accion = accion
        self.padre=padre
        self.costo=costo

    def imprimir(self):
        print(self.estado, self.accion , self.padre, self.costo)
        