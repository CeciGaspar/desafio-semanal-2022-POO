# Crea una única función (importante que sólo sea una) que sea capaz de calcular y 
# retornar el área de un polígono. 
#- La función recibirá por parámetro sólo UN polígono a la vez.
#- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#- Imprime el cálculo del área de un polígono de cada tipo.

base = int(input("Ingrese el valor de base"))
altura = int(input("Ingrese el valor de la altura"))
tipoPoligono = str(input("Ingrese el tipo de poligono"))

def areaPoligono(pbase, paltura, ppoligono):
    if ppoligono == "triangulo" or ppoligono == "rectangulo" or ppoligono == "cuadrado":
        if ppoligono == "triangulo":
            area = (pbase * paltura/2)
            print(f"el area del {ppoligono} es: {area}")
        else:
            area= (pbase * paltura)
            print(f"el area del {ppoligono} es {area}")
    else:
        print("ha ingresado una figura geometrica incorrecta")

areaPoligono(base,altura,tipoPoligono)
