
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTabWidget
from Caja import Caja


class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        pestanas = QTabWidget()
        pestanas.addTab(Caja('Red'), 'Rojo')
        pestanas.addTab(Caja('Yellow'), 'Amarillo')
        pestanas.addTab(Caja('Pink'), 'Rosa')

        pestanas.setTabPosition(QTabWidget.South)
        pestanas.setMovable(True)
        self.setCentralWidget(pestanas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
