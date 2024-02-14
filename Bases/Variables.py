from Varias import nuevo_tema

nuevo_tema("Variables")

edad = 23
print('edad: ', edad)

altura = 1.7
print('altura: ', altura)

nombre = "Panchito"
print('nombre: ', nombre)

fuma = False
print('fuma: ', fuma)


nuevo_tema("Instrucciones de control")

def nuevo_subtema(subtema:str = ''):
    print('-------------', subtema)

nuevo_subtema('if-else')

numeroA = 44
numeroB = 8

if numeroA > numeroB:
    print(numeroA, "es mayor que", numeroB)

if numeroA < numeroB:
    print(numeroA, "es menor que", numeroB)

if numeroA == numeroB:
    print(numeroA, "es igual", numeroB)

nuevo_tema("ciclos")
nuevo_subtema('for')

for i in range(5):
    print(i)