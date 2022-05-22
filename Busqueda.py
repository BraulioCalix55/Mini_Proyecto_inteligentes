from Colonia import Colonia
from Ciudad import Ciudad

class Busqueda:
    
    ciudad=None,
    costoFinal = 0.0,
    rutas=[]

    def cargarRutas(ruta):
        with open("./"+ruta) as contenido:
            
            costoTotal=contenido.readline()
            ciudadInicial= contenido.readline()
            destinos=[]
            print(costoTotal)
            print(ciudadInicial)
            
            

           
