import json
class File:
     
    def iniciar():
        print("iniciar")
        
    def cargar(self):
        with open('./Mapa.json') as contenido:
            mapa=json.load(contenido)
            for i in mapa:
                print("----------------------------------")
                print(i.get("nombre"))
                print (i.get("nombre"))
      