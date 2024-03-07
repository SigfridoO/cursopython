
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QComboBox

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        desplegable = QComboBox()
        desplegable.addItems(['','opcion 1', 'opcion 2', 'opcion 3', 'opcion 4', 'opcion 5'])
        desplegable.currentTextChanged.connect(self.cambiar_texto)
        desplegable.currentIndexChanged.connect(self.cambiar_indice)
        self.setCentralWidget(desplegable)

    def cambiar_texto(self, texto):
        print(texto)

    def cambiar_indice(self, indice):
        print(indice)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
