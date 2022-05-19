from Nodo import Nodo
class Cola:


    cola=[]

    def isEmpty(self):
        if len(self.cola) <=0:
            return False
        else:    
            return True

    def pop(self):
        return self.cola.pop(0)

    def top(self):
        return self.cola[0]

    def add(self, elemento):
        self.cola.append(elemento)

    def imprimirCola(self):
        print(self.cola)

