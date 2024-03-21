
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
        QWidget, QStatusBar, QAction, QMessageBox
from PyQt5.QtGui import QIcon

def absPath(nombre):
    return str(  Path(__file__).parent.absolute()/ nombre )


class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.resize(600, 400)
        self.setStatusBar(QStatusBar(self))
        icono = QIcon(absPath('gato.jpeg'))
        self.setWindowIcon(icono)

        self.construir_menu()

    def construir_menu(self):
        menu = self.menuBar()
        menuArchivo = menu.addMenu("&Archivo")
        menuArchivo.addAction("A&brir")
        submenu = menuArchivo.addMenu("Sub&menu")
        submenu.addAction("Opción &1")
        submenu.addAction("Opción &2")
        submenu.addSeparator()

        actionMensaje = QAction("Men&saje", self)
        actionMensaje.setIcon(QIcon(absPath('gato.jpeg')))
        actionMensaje.setShortcut('Ctrl-m')
        actionMensaje.triggered.connect(self.mostrar_mensaje)
        menuArchivo.addAction(actionMensaje)
        menuArchivo.setStatusTip("Un comando informativo")

        menuArchivo.addAction(QIcon(absPath('gato.jpeg')), "Salir", self.close, "Ctrl+d")

        menuEditar = menu.addMenu("&Editar")
    def mostrar_mensaje(self):
        print("mostrando el mensaje")
        QMessageBox.information(self, "Informacion", "texto informativo")
        #QMessageBox.warning(self, "Informacion", "texto informativo")
        #QMessageBox.critical(self, "Informacion", "texto informativo")
        #QMessageBox.question(self, "Informacion", "texto informativo")
        #QMessageBox.about(self, "Informacion", "texto informativo")
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
