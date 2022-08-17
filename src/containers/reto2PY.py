"""
Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
* La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
* 0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci_iter(n):
    a = 1
    b = 1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b = a
            a = total
            print(total)
         
fibonacci_iter(50)





