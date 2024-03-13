
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QStackedLayout
from Caja import Caja

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        layout = QStackedLayout()
        layout.addWidget(Caja('Red'))
        layout.addWidget(Caja('Green'))
        layout.addWidget(Caja('Yellow'))
        layout.addWidget(Caja('Blue'))
        layout.addWidget(Caja('Orange'))

        widget = QWidget()
        widget.setLayout(layout)

        self.layout = layout

        self.setCentralWidget(widget)

    def keyPressEvent(self, event):

        indice = self.layout.currentIndex()
        indiceMaximo = self.layout.count() - 1

        if event.key() == Qt.Key_Right:
            indice += 1

        if event.key() == Qt.Key_Left:
            indice -= 1

        if indice < 0:
            indice = indiceMaximo
        if indice > indiceMaximo:
            indice = 0

        self.layout.setCurrentIndex(indice)

        print(indice, indiceMaximo)

        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
