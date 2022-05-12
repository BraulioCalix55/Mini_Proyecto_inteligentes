class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def saludo(self,mensaje):
        print(mensaje)
    def toString(self):
        return self.nombre,self.edad,self.sexo

    
        