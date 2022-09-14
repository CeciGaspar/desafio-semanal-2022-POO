simbolosPuntuacion = [",", ";", ":", ".", "·", "¿", "?", "¡", "!", "(", ")", "-", "_", "<", ">", "*", "'", "{", "}","[", "]", "^", "%", "/", "|", "\\"]
acentos = {"á": "a","à": "a","ä": "a","â": "a","é": "e","è": "e","ë": "e","ê": "e","í": "i","ì": "i","ï": "i","î": "i","ó": "o","ò": "o","ö": "o","ô": "o","ú": "u","ù": "u","ü": "u","û": "u"}

def eliminarCaracters(frase: str) -> str:
    fraseSinCarac = frase.lower()

    for carac in frase.lower():
        if carac in simbolosPuntuacion:
            fraseSinCarac = fraseSinCarac.replace(carac, "")

        if carac in acentos.keys():
            fraseSinCarac = fraseSinCarac.replace(carac, acentos[carac])

    return fraseSinCarac.replace(" ", "")

def palindromos(frase: str) -> bool:
    limpiarFrase = eliminarCaracters(frase)
    fraseAlReves = ""

    for carac in limpiarFrase[::-1]:
        fraseAlReves += carac

    if limpiarFrase == fraseAlReves:
        return True
    else:
        return False

print(palindromos("Ana lleva al oso la avellana."))
print(palindromos("Argentina Campeón"))
