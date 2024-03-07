
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.texto = QLineEdit()
        self.texto.returnPressed.connect(self.texto_presionado)
        self.texto.textChanged.connect(self.texto_cambiado)
        self.setCentralWidget(self.texto)

    def texto_presionado(self):
        texto = self.texto.text()
        print("El texto introducido es:", texto)
        
    def texto_cambiado(self, texto):
        print(texto)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
