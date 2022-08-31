#Enunciado: Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y 
#que muestre el recuento final de todas ellas. - Los signos de puntuación no forman parte de 
#la palabra. - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas. 
#- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

palabras = "HOLA MUNDO hola MUNDO hola mundo"
palabras = palabras.lower()
palabras = palabras.split(" ")
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
        print(diccionario_frecuencias[palabra])
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' se repite {frecuencia} veces")
