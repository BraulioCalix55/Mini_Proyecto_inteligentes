import json
class Menu:
    def __init__(self,valor):
        self.valor=valor
    
    def iniciar():
        print("iniciar")
    def cargar(self):
        with open('./Nodos.json') as contenido:
            nodos=json.load(contenido)
            for nodos in nodos:
                print (nodos.get("nombre"))
            
        
       
        