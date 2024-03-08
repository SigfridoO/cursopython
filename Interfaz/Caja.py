
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')



class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        caja = Caja('green')
        self.setCentralWidget(caja)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
