import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from GUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.stackedWidget.setCurrentWidget(self.uic.Home)
        self.uic.Btn_Home.clicked.connect(self.showScreen_Home)
        self.uic.Btn_Page_1.clicked.connect(self.showScreen_1)
        self.uic.Btn_Page_2.clicked.connect(self.showScreen_2)       
        self.uic.Btn_Exit.clicked.connect(self.main_win.close)
    def show(self):
        self.main_win.show()
    def showScreen_Home(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Home)
    def showScreen_1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Screen_1)
    def showScreen_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Screen_2)

if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())