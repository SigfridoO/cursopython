def crearMenu():
    print("-----------------------------")
    print('Programa que calcula el área de figuras geométricas')
    print('Elige una opcion')
    print("-----------------------------")
    print('1. Cuadrado')
    print('2. Círculo')
    print('0. Salir')

    print('\n\nPor favor elige una opción: ')
    opcion = input()
    print('La opcion elegida es:', opcion)

def main():
    crearMenu()

if __name__ == "__main__":
    main()