# main.py

import sys
from PyQt5.QtWidgets import QApplication
from Vistas.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
