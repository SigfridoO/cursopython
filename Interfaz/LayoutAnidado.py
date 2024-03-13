
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout

from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        caja1 = Caja('red')
        caja2 = Caja('blue')
        caja3 = Caja('yellow')
        caja4 = Caja('pink')
        caja5 = Caja('green')
        caja6 = Caja('gray')
        
        layoutHorizontal1 =  QHBoxLayout()
        layoutVertical1 = QVBoxLayout()
        layoutHorizontal2 = QHBoxLayout()

        layoutHorizontal1.addWidget(caja1)
        layoutHorizontal1.addLayout(layoutVertical1)

        layoutVertical1.addWidget(caja2)
        layoutVertical1.addWidget(caja3)
        layoutVertical1.addLayout(layoutHorizontal2)

        layoutHorizontal2.addWidget(QPushButton("Aceptar"))
        layoutHorizontal2.addWidget(QPushButton("Cancelar"))
        layoutHorizontal2.addWidget(QPushButton("OK"))
    
        widget = QWidget()
        widget.setLayout(layoutHorizontal1)
        
        self.setCentralWidget(widget)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
