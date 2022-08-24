# Escribe un programa que se encargue de comprobar si un número es o no primo. 
# Hecho esto, imprime los números primos entre 1 y 100.

num = int(input("Ingrese un número: "))

def primo(número):
  for i in range(2,número):
    if (número%i) == 0:
      return False
  return True

print(primo(num))

numero = 1
while numero <= 100:
    contador = 1
    x = 0
    while contador <= numero:
        if numero % contador == 0:
            x = x + 1
        contador = contador + 1
    if x == 2:
        print(numero)
    numero = numero + 1

