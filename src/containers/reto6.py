#Enunciado: Enunciado: Crea un programa que invierta el orden de una 
#cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática. 
#- Si le pasamos 'Hola mundo' nos retornaría 'odnum aloH'

cadena = "Hola Mundo"
alReves=[]
cantIndex = len(cadena)
while cantIndex > 0: 
    alReves += cadena[cantIndex-1]
    cantIndex = cantIndex - 1 # decrement index
    imprimir = "".join(alReves)
print(imprimir) 
