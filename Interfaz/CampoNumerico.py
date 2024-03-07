
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDoubleSpinBox

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        numero = QDoubleSpinBox()
        #numero.setMaximum(8)
        #numero.setMinimum(-3)
        numero.setRange(-3, 8)
        numero.setPrefix("Temp: ")
        numero.setSuffix("º")
        numero.setSingleStep(0.5)
        numero.valueChanged.connect(self.valor_cambiado)

        self.setCentralWidget(numero)

    def valor_cambiado(self, valor):
        print(valor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
º