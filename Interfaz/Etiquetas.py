
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel

def absPath(nombre):
    return str(  Path(__file__).parent.absolute()/ nombre )

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        etiqueta = QLabel('Soy una etiqueta')        
        self.setCentralWidget(etiqueta)
        fuente = QFont('Manjari', 24)
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        imagen = QPixmap(absPath('gato.jpeg'))
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
