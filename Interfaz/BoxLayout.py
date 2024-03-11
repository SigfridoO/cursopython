
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        caja1 = Caja('red')
        caja2 = Caja('blue')
        caja3 = Caja('yellow')
        
        layout =  QHBoxLayout()
        layout.addWidget(caja1)
        layout.addWidget(caja2)
        layout.addWidget(caja3)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
