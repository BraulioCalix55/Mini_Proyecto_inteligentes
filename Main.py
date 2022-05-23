from Busqueda import Busqueda
import sys
import time

def menu():
    print("\n\n1) BFS")
    print("2) Busqueda de Costo Uniforme")
    print("3) A*")
    print("4) Salir")
    opcion = int(input("Ingrese una opcion:\n"))
    return opcion

def leerArchivoProblema(nombreArchivo):
    with open(nombreArchivo, "r") as archivo:
        datos = archivo.readlines()
    return datos

def crearEntrega():
    datosArchivo = leerArchivoProblema(sys.argv[2]) #El txt de las colonias a visitar
    entregas = []
    for indice, dato in enumerate(datosArchivo):
        if indice == 0:
            costoMaximo = float(dato.strip()) #La Primera linea es el costo maximo
        elif indice == 1:
            ubicacionInicial = dato.strip() # La segunda linea es la colonia del inicio del recorrido
        else:
            entregas.append(dato.strip()) # Se cargan las colonias a visitar
    return Busqueda(ubicacionInicial, entregas, costoMaximo)    

def main():
    entrega= crearEntrega()
    entrega.cargarMapa(sys.argv[1]) #Sys.argvs[1] es el Json del mapa

    opcion = 0
    while opcion != 4:        
        opcion = menu()
        if opcion == 1:
            timeInicio = time.time()
            entrega.BFS()
            timeFinal = time.time()
            timeT = timeFinal - timeInicio
            print("A la busqueda BFS le tomo %s segundos" % (timeT))
        if opcion == 2:
            timeInicio = time.time()
            entrega.costoUniforme()
            timeFinal = time.time()
            timeT = timeFinal - timeInicio
            print("A la busqueda de costo uniforme le tomo %s segundos" % (timeT))
        elif opcion == 3:
            print("No implementado")
            

if __name__ == "__main__":
    main()