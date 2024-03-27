
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, \
        QWidget, QPlainTextEdit, QFormLayout, \
        QPushButton, QCheckBox, QRadioButton, QLineEdit, QLabel, QDial, QVBoxLayout

class EditorQSS(QWidget):
    def __init__(self, parent):
        super().__init__() 
        self.parent = parent
        self.resize(420, 300)

        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.actualizar_editor)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.show()

    def actualizar_editor(self):
        qss = self.editor.toPlainText()
        


class Ventana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        layout = QFormLayout()

        layout.addRow('QPushButton', QPushButton())
        layout.addRow('QLabel', QLabel())
        layout.addRow('QLineEdit', QLineEdit())
        layout.addRow('QCheckBox', QCheckBox())
        layout.addRow('QRadioButton', QRadioButton())
        layout.addRow('QDial', QDial())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        self.editorQSS = EditorQSS(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show();
    sys.exit(app.exec())
       
