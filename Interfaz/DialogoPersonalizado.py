
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
      QWidget, QDialog, QHBoxLayout, QDialogButtonBox

class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Soy un dialog")
        self.resize(460,300)
        layout = QHBoxLayout()

        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(botones)

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")

        self.setLayout(layout)
        


class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        boton = QPushButton("Abrir Dialog")
        boton.clicked.connect(self.abrir_ventana)
        self.setCentralWidget(boton)

    def abrir_ventana(self):
        print ("Dentro de abrir ventana")
        dialogo = Dialogo()
        respuesta = dialogo.exec()
        if respuesta:
            print('Dialogo aceptado')
        else:
            print('Dialogo rechazado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
