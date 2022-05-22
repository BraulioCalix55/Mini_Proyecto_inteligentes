import json
from Ciudad import Ciudad
from Colonia import Colonia
class File:
     
    def iniciar():
        print("iniciar")
        
    def cargar(ruta):
        with open("./"+ruta) as contenido:
            mapa=json.load(contenido)
            ciudad = Ciudad(mapa.get("Ciudad"))
            colonias = mapa.get("Colonias")
            for elemento in colonias:  
                
                ciudad.agregarColonia(Colonia.crearColonia(elemento))
            
            print(ciudad)
            '''A este punto, se crea un nodo llamado Ciudad que tiene de atributo un nombre que es Tegucigalpa,
            y este a su vez, tiene nodos llamados Colonias que tiene toda la información de las Colonias, tanto su nombre 
            y el costo que tiene viajar de una colonia a otra, justo como está en el Json'''

           

            
            
            

      