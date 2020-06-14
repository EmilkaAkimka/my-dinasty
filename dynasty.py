import sys
from PyQt5.QtWidgets import QApplication, QMainWindow



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Tech With Timi")

    win.show()
    sys.exit(app.exec_())

window()