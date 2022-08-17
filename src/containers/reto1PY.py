"""
Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
* Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
* NO hace falta comprobar que ambas palabras existan.
* Dos palabras exactamente iguales no son anagrama.
"""
palabra1 = "NEPAL"
palabra2 = "PANEL"

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1list = list(palabra1)
    palabra2list = list(palabra2)
    palabra1list.sort()
    palabra2list.sort()
    palabra1_ordenada = "".join(palabra1list)
    palabra2_ordenada = "".join(palabra2list)
    return palabra1_ordenada == palabra2_ordenada

print(anagrama(palabra1, palabra2))