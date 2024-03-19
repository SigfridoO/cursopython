
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
      QWidget, QFileDialog, QFontDialog, QColorDialog

class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.boton = QPushButton("Abrir")
        self.setCentralWidget(self.boton)
        self.boton.clicked.connect(self.abrir)

    def abrir(self):
        print("Realizando una acción sumamente importante")
        #archivo = QFileDialog.getOpenFileName(self, "Abrir archivo", ".")
        #archivo = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        #print(archivo)

        #fuente , confirmado = QFontDialog.getFont(self)
        #if confirmado:
        #    self.boton.setFont(fuente)

        color = QColorDialog.getColor()
        print(color)
        
        if color.isValid:
            self.boton.setStyleSheet(f"background-color: {color.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
