from array import array
from Persona import Persona
secretario = Persona("mario",55,"")
arreglo=[]
arreglo.append(5)
arreglo.append("hola")
arreglo.append(secretario)
arreglo.append(Persona("juan",31,"hombre"))
arreglo.append(Persona("miguel",31,""))
b="hpla"
arreglo.append([b,4,1])
for i in arreglo :
    if isinstance(i,Persona) and i.nombre=="miguel":
       i.sexo="hombre"
    if isinstance(i,Persona):
       print( i.toString())
    else:
        print(i)
        
    

