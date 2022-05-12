from Menu import Menu
class Main:
   def __init__(self):
      menu=True
      while(menu):
         print("MINI PROYECTO #1")
         print("----------------\nBraulio Calix Montesinos--11711133\nDavid Mejia Flores--11811310")
         print("----------------")       
         print("1) Cargar Mapa \n2)Iniciar Busqueda")
         opcion=0
         opcion=input()
         opcion=int(opcion)
         #aprendi que para hacer buen manejo de los menus, o se castea la entrada, o donde se verifique la entrada, se debe de poner 'valor'
         if (opcion == 1):
            Menu(opcion)
            Menu.cargar(0)
         elif(opcion==2):
            Menu.iniciar()
         else :
            print ("se ingreso un valor incorrecto")
            
         print("Presione 1 si desea reingresar al mini proyecto")
         menu=input()
         menu=int(menu)
         if(menu!= 1):
            menu=False
      print("Hasta luego")
         
         

