
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout

from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        layout = QGridLayout()
        layout.addWidget(Caja('blue'), 0, 0, 2, 1)            # Fila 0, col 0
        layout.addWidget(Caja('magenta'), 1, 1)         # Fila 1, col 1
        layout.addWidget(Caja('orange'), 2, 1)          # Fila 2, col 1

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
