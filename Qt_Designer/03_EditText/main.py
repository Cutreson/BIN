import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from GUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Btn_Start.clicked.connect(self.showHello)
        self.uic.Btn_Copy.clicked.connect(self.copytext)
        self.uic.Btn_Stop.clicked.connect(self.exit)
    def show(self):
        self.main_win.show()
    def showHello(self):
        self.uic.Label.setText("Hello")
    def copytext(self):
        copy = self.uic.Edit_Text.toPlainText()
        self.uic.Label.setText(copy)
    def exit(self):
        self.main_win.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
