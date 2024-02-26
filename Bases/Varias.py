def nuevo_tema(tema:str = ""):
    print("===================", tema, "===================")

def nuevo_subtema(subtema:str = ''):
    print('-------------', subtema)

def comparar(numeroA:int, numeroB:int):

    if numeroA > numeroB:
        print(numeroA, "es mayor que", numeroB)

    if numeroA < numeroB:
        print(numeroA, "es menor que", numeroB)

    if numeroA == numeroB:
        print(numeroA, "es igual", numeroB)

def sumar(*args) -> int:
    print('Los numeros a sumar son')

    suma = 0
    for numero in args:
        print(numero)
        suma += numero

    
    return suma