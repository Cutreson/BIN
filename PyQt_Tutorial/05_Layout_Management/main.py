import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Hello")
    b. move(50,20)
    w.setGeometry(10,10,300,200)
    w.setWindowTitle("Hello")
    w.show()
    sys.exit(app.exec())
if __name__=="__main__":
    window()