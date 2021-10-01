# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(120, 50, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.Label.setFont(font)
        self.Label.setAutoFillBackground(False)
        self.Label.setStyleSheet("")
        self.Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Label.setLineWidth(1)
        self.Label.setMidLineWidth(0)
        self.Label.setOpenExternalLinks(False)
        self.Label.setObjectName("Label")
        self.Edit_Text = QtWidgets.QTextEdit(self.centralwidget)
        self.Edit_Text.setGeometry(QtCore.QRect(120, 140, 341, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Edit_Text.setFont(font)
        self.Edit_Text.setObjectName("Edit_Text")
        self.Btn_Start = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Start.setGeometry(QtCore.QRect(90, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Btn_Start.setFont(font)
        self.Btn_Start.setObjectName("Btn_Start")
        self.Btn_Copy = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Copy.setGeometry(QtCore.QRect(250, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Btn_Copy.setFont(font)
        self.Btn_Copy.setObjectName("Btn_Copy")
        self.Btn_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Stop.setGeometry(QtCore.QRect(410, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Btn_Stop.setFont(font)
        self.Btn_Stop.setObjectName("Btn_Stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Label.setText(_translate("MainWindow", "Display"))
        self.Btn_Start.setText(_translate("MainWindow", "Start"))
        self.Btn_Copy.setText(_translate("MainWindow", "Copy"))
        self.Btn_Stop.setText(_translate("MainWindow", "Stop"))

