def numeroARMSTRONG(numero: int):
    numStr = str(numero)
    numFinal = 0

    for num in numStr:
        numFinal += int(num) ** len(numStr)

    if numFinal == numero:
        return True
    else:
        return False

print(numeroARMSTRONG(371))
print(numeroARMSTRONG(2015))