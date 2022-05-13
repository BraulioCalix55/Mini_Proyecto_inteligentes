import json
class Menu:
    def __init__(self,valor):
        self.valor=valor
    
    def iniciar():
        print("iniciar")
    def cargar(self):
        with open('./Mapa.json') as contenido:
            mapa=json.load(contenido)
            for mapa in mapa:
                print("----------------------------------")
                print(mapa.get("nombre"))
                print (mapa.get("vecinos"))
                ###HAY QUE CREAR EL OBJETO NODO       