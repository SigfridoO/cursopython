
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
        QWidget, QCheckBox

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        casilla = QCheckBox('Casilla')
        casilla.stateChanged.connect(self.modificarEstado)

        self.setCentralWidget(casilla)

    def modificarEstado(self, estado):
        print (estado)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
