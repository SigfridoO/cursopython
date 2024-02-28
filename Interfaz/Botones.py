
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Hola mundo')
        self.resize(480,300)
        self.setMaximumSize(600,400)
        self.setMinimumSize(280, 100)

        boton = QPushButton('Soy un boton')
        self.setCentralWidget(boton)

        #boton.clicked.connect(self.clickear)
        #boton.pressed.connect(self.presionar)
        #boton.released.connect(self.liberar)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)
        self.boton = boton

    def presionar(self):
        print('boton presionado')

    def liberar(self):
        print('boton liberado')

    def clickear(self):
        print('boton clickeado')
        
    def boton_alternado(self, valor):
        print(valor)
        if valor:
            self.boton.setText('Estoy presionado')
        else:
            self.boton.setText('Estoy liberado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
