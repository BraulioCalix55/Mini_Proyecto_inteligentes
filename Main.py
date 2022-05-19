from File import File

def opciones ():
   print("\n\n1MINI PROYECTO #1")
   print("----------------\nBraulio Calix Montesinos--11711133\nDavid Mejia Flores--11811310")
   print("----------------")       
   print("1) Cargar Mapa \n2) BFS\n3) Costo Uniforme\n4) A*\n5) Salir")
   print("Elija una opción")


menu=True
while(menu):
   opciones()
   opcion=int(input())
   
   if (opcion == 1):
      m = File.cargar(0)
   elif(opcion==2):
      print(" BFS")
   elif (opcion==3):
      print("Costo uniforme")
   elif (opcion==4):
      print("A*")
   elif (opcion==5):
      print("Adios...")
      menu = False
      exit()
   else :
      print ("Se ingresó una opción incorrecta.")






         
         

