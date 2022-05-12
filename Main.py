from Menu import Menu
menu=True
while(menu):
   print("MINI PROYECTO #1")
   print("----------------\nBraulio Calix Montesinos--11711133\nDavid Mejia Flores--11811310")
   print("----------------")       
   print("1) Cargar Mapa \n2)Iniciar Busqueda")
   opcion=0
   opcion=input()
   opcion=int(opcion)
   #aprendi que para hacer buen manejo de los menus, o sea castea la entrada, o donde se verifique la entrada, se debe de poner 'valor'
   if (opcion == 1):
      print ("aqui es 1")
      Menu.abrir(1)
      Menu.leer(1)
   elif (opcion == 2):
      print ("aqui es 2")
      print("iniciar")
  
   print("Presione 1 si desea reingresar al mini proyecto")
   menu=input()
   menu=int(menu)
   if(menu!= 1):
      menu=False
print("Hasta luego")
   
    

