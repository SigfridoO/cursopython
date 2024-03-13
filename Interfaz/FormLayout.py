
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFormLayout
from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        layout = QFormLayout()
        layout.addRow('Magenta', Caja('Magenta'))
        layout.addRow('Red', Caja('Red'))
        layout.addRow('Yellow', Caja('Yellow'))
        layout.addRow('Green', Caja('Green'))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
