from Varias import nuevo_tema, nuevo_subtema, comparar, \
    sumar

nuevo_tema("Variables")

edad = 23
print('edad: ', edad)

altura = 1.7
print('altura: ', altura)

nombre = "Panchito"
print('nombre: ', nombre)

fuma = False
print('fuma: ', fuma)

nuevo_subtema('Listas')
miListaDeFrutas = ['manzanas', 'platanos', 'guayabas', 'naranjas', 'sandias', 'duraznos']
print ('miListaDeFrutas: ', miListaDeFrutas)

miListaDeFrutas.append('uvas')
print ('miListaDeFrutas: ', miListaDeFrutas)

miListaDeFrutas.remove('platanos')
print ('miListaDeFrutas: ', miListaDeFrutas)

miListaDeFrutas.insert(3, 'papayas')
print ('miListaDeFrutas: ', miListaDeFrutas)

print ('miListaDeFrutas[2]: ', miListaDeFrutas[2])

print ('miListaDeFrutas[2:5]', miListaDeFrutas[2:5])

print ('miListaDeFrutas[1:6:2]', miListaDeFrutas[1:6:2])

print ('miListaDeFrutas[:]', miListaDeFrutas[:])

print ('miListaDeFrutas[-1]', miListaDeFrutas[-1])


print ('miListaDeFrutas: ', miListaDeFrutas)
miListaDeFrutas.reverse()
print ('miListaDeFrutas.reverse()', miListaDeFrutas)

miListaDeFrutas.sort()
print ('miListaDeFrutas.sort()', miListaDeFrutas)


print('longitud de la lista', len(miListaDeFrutas)  )
# Recorriendo una lista con un for
for fruta in miListaDeFrutas:
    print (fruta)


miLista2 = ['casas', 25, 1.8 ,'caminar', True]
print ('miLista2: ', miLista2)

#--------------------- diccionarios
nuevo_subtema('diccionario')

miPrimerDiccionario = dict()

miSegundoDiccionario = {'nombre': "Pancho", 'edad': 25, 
    "altura": 1.4 , "Observaciones": "no da clase"}

print("miPrimerDiccionario : ", miPrimerDiccionario)
print("miSegundoDiccionario: ", miSegundoDiccionario)

# seleccionando un elemento
print("miSegundoDiccionario.get('nombre') = ", 
    miSegundoDiccionario.get('nombre'))

# agregando un elemento
print("miPrimerDiccionario : ", miPrimerDiccionario)
miPrimerDiccionario.update({"mexico": "tecolotitos de tlaxcala"})
print("miPrimerDiccionario : ", miPrimerDiccionario)

# obteniendo valores
print("miSegundoDiccionario.values(): ", miSegundoDiccionario.values())
# obteniendo llaves
print("miSegundoDiccionario.keys(): ", miSegundoDiccionario.keys())

# recorriendo un diccionario con for
for key, value in miSegundoDiccionario.items():
    print (key , ":", value)



nuevo_tema("Instrucciones de control")



nuevo_subtema('if-else')

numeroA = 44
numeroB = 8

comparar(numeroA, numeroB)

nuevo_tema("ciclos")
nuevo_subtema('for')

for i in range(5):
    print(i)


def crearMenu():
    print("-----------------------------")
    print('Programa que calcula el área de figuras geométricas')
    print('Elige una opcion')
    print("-----------------------------")
    print('1. Cuadrado')
    print('2. Círculo')
    print('0. Salir')

nuevo_subtema('while')
condicion = True
contador = 0
crearMenu()
while condicion:



    print ('La condicion es ', condicion, contador)
    contador = contador +1

    if contador > 5:
        condicion = False









nuevo_subtema('do-while')


nuevo_tema('Funciones')
print ("La suma es: ",  sumar(numeroA, numeroB, 1, 2,  3, 4, 5,))
