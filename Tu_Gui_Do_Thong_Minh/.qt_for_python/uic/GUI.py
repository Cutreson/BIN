# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Tu_gui_do\Code\output\main\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(0, 0, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Home = QtWidgets.QWidget()
        self.tab_Home.setObjectName("tab_Home")
        self.label = QtWidgets.QLabel(self.tab_Home)
        self.label.setGeometry(QtCore.QRect(0, 20, 971, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_Tu_1 = QtWidgets.QPushButton(self.tab_Home)
        self.btn_Tu_1.setGeometry(QtCore.QRect(50, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Tu_1.setFont(font)
        self.btn_Tu_1.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_Tu_1.setObjectName("btn_Tu_1")
        self.label_Tu_1 = QtWidgets.QLabel(self.tab_Home)
        self.label_Tu_1.setGeometry(QtCore.QRect(10, 140, 201, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tu_1.setFont(font)
        self.label_Tu_1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_Tu_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tu_1.setObjectName("label_Tu_1")
        self.btn_Tu_2 = QtWidgets.QPushButton(self.tab_Home)
        self.btn_Tu_2.setGeometry(QtCore.QRect(300, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Tu_2.setFont(font)
        self.btn_Tu_2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_Tu_2.setObjectName("btn_Tu_2")
        self.label_Tu_2 = QtWidgets.QLabel(self.tab_Home)
        self.label_Tu_2.setGeometry(QtCore.QRect(260, 140, 201, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tu_2.setFont(font)
        self.label_Tu_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_Tu_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tu_2.setObjectName("label_Tu_2")
        self.btn_Tu_3 = QtWidgets.QPushButton(self.tab_Home)
        self.btn_Tu_3.setGeometry(QtCore.QRect(790, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Tu_3.setFont(font)
        self.btn_Tu_3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_Tu_3.setObjectName("btn_Tu_3")
        self.btn_Tu_4 = QtWidgets.QPushButton(self.tab_Home)
        self.btn_Tu_4.setGeometry(QtCore.QRect(540, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Tu_4.setFont(font)
        self.btn_Tu_4.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_Tu_4.setObjectName("btn_Tu_4")
        self.label_Tu_4 = QtWidgets.QLabel(self.tab_Home)
        self.label_Tu_4.setGeometry(QtCore.QRect(750, 140, 201, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tu_4.setFont(font)
        self.label_Tu_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_Tu_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tu_4.setObjectName("label_Tu_4")
        self.label_Tu_3 = QtWidgets.QLabel(self.tab_Home)
        self.label_Tu_3.setGeometry(QtCore.QRect(500, 140, 201, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tu_3.setFont(font)
        self.label_Tu_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_Tu_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Tu_3.setObjectName("label_Tu_3")
        self.label_display = QtWidgets.QLabel(self.tab_Home)
        self.label_display.setGeometry(QtCore.QRect(0, 470, 981, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_display.setFont(font)
        self.label_display.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(255, 0, 0);")
        self.label_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_display.setObjectName("label_display")
        self.tabWidget.addTab(self.tab_Home, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 971, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.btn_delete_One = QtWidgets.QPushButton(self.tab)
        self.btn_delete_One.setGeometry(QtCore.QRect(720, 80, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete_One.setFont(font)
        self.btn_delete_One.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_delete_One.setObjectName("btn_delete_One")
        self.table_Data = QtWidgets.QTableWidget(self.tab)
        self.table_Data.setEnabled(True)
        self.table_Data.setGeometry(QtCore.QRect(120, 80, 571, 451))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.table_Data.setFont(font)
        self.table_Data.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.table_Data.setLineWidth(1)
        self.table_Data.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_Data.setAutoScroll(True)
        self.table_Data.setAutoScrollMargin(10)
        self.table_Data.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_Data.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_Data.setShowGrid(True)
        self.table_Data.setGridStyle(QtCore.Qt.SolidLine)
        self.table_Data.setCornerButtonEnabled(True)
        self.table_Data.setRowCount(30)
        self.table_Data.setObjectName("table_Data")
        self.table_Data.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_Data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_Data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_Data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(185)
        item.setFont(font)
        self.table_Data.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.table_Data.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.table_Data.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.table_Data.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.table_Data.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Data.setItem(6, 2, item)
        self.table_Data.horizontalHeader().setVisible(False)
        self.table_Data.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Data.horizontalHeader().setDefaultSectionSize(185)
        self.table_Data.horizontalHeader().setHighlightSections(False)
        self.table_Data.horizontalHeader().setMinimumSectionSize(30)
        self.table_Data.horizontalHeader().setSortIndicatorShown(False)
        self.table_Data.horizontalHeader().setStretchLastSection(False)
        self.table_Data.verticalHeader().setVisible(False)
        self.table_Data.verticalHeader().setCascadingSectionResizes(False)
        self.table_Data.verticalHeader().setDefaultSectionSize(185)
        self.table_Data.verticalHeader().setMinimumSectionSize(30)
        self.btn_delete_All = QtWidgets.QPushButton(self.tab)
        self.btn_delete_All.setGeometry(QtCore.QRect(720, 150, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete_All.setFont(font)
        self.btn_delete_All.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border-color: rgb(255, 0, 0);")
        self.btn_delete_All.setObjectName("btn_delete_All")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tủ gửi đồ thông minh"))
        self.label.setText(_translate("MainWindow", "Tủ gửi đồ thông minh sử dụng trí tuệ nhân tạo"))
        self.btn_Tu_1.setText(_translate("MainWindow", "Mở khóa"))
        self.label_Tu_1.setText(_translate("MainWindow", "Tủ số 1"))
        self.btn_Tu_2.setText(_translate("MainWindow", "Mở khóa"))
        self.label_Tu_2.setText(_translate("MainWindow", "Tủ số 2"))
        self.btn_Tu_3.setText(_translate("MainWindow", "Mở khóa"))
        self.btn_Tu_4.setText(_translate("MainWindow", "Mở khóa"))
        self.label_Tu_4.setText(_translate("MainWindow", "Tủ số 4"))
        self.label_Tu_3.setText(_translate("MainWindow", "Tủ số 3"))
        self.label_display.setText(_translate("MainWindow", "Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Home), _translate("MainWindow", "Trang chủ"))
        self.label_5.setText(_translate("MainWindow", "Danh sách những người quên chưa lấy đồ"))
        self.btn_delete_One.setText(_translate("MainWindow", "Xóa hàng"))
        self.table_Data.setSortingEnabled(False)
        item = self.table_Data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hình ảnh"))
        item = self.table_Data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Số tủ"))
        item = self.table_Data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Thời gian"))
        __sortingEnabled = self.table_Data.isSortingEnabled()
        self.table_Data.setSortingEnabled(False)
        self.table_Data.setSortingEnabled(__sortingEnabled)
        self.btn_delete_All.setText(_translate("MainWindow", "Xóa tất cả"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Lịch sử"))
