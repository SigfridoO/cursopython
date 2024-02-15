from Varias import nuevo_tema, nuevo_subtema

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

miLista2 = ['casas', 25, 1.8 ,'caminar', True]
print ('miLista2: ', miLista2)

nuevo_tema("Instrucciones de control")



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


nuevo_subtema('while')


nuevo_subtema('do-while')