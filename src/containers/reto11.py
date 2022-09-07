cadena1 = input("ingrese una cadena: ")
cadena2 = input("ingrese 2da cadena cadena:")

def invertirCadenas(cadena1,cadena2):
    Out1 = ""
    Out2 = ""

    for letra in cadena1:
        if not letra in cadena2:
            Out1 += f"{letra}"

    for letra in cadena2:
        if not letra in cadena1:
            Out2 += f"{letra}"

    print(f"los caracteres presentes en el str1 pero no estan presentes en el str2 son: {Out1}")
    print(f"los caracteres presentes en el str2 pero no estan presentes en el str1 son: {Out2}")    

invertirCadenas(cadena1,cadena2)