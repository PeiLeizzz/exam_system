# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mock_test_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MockTestWindow(object):
    def setupUi(self, MockTestWindow):
        MockTestWindow.setObjectName("MockTestWindow")
        MockTestWindow.resize(853, 594)
        self.centralwidget = QtWidgets.QWidget(MockTestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 60, 531, 311))
        self.textEdit.setObjectName("textEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(320, 410, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 410, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(570, 410, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(720, 410, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 460, 93, 28))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 460, 93, 28))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 510, 93, 28))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(320, 410, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(450, 410, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(570, 410, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(720, 410, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(450, 410, 115, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(570, 410, 115, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(570, 580, 115, 19))
        self.radioButton_7.setObjectName("radioButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 241, 311))
        self.listWidget.setObjectName("listWidget")
        MockTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MockTestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 26))
        self.menubar.setObjectName("menubar")
        MockTestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MockTestWindow)
        self.statusbar.setObjectName("statusbar")
        MockTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MockTestWindow)
        QtCore.QMetaObject.connectSlotsByName(MockTestWindow)

    def retranslateUi(self, MockTestWindow):
        _translate = QtCore.QCoreApplication.translate
        MockTestWindow.setWindowTitle(_translate("MockTestWindow", "MainWindow"))
        self.radioButton.setText(_translate("MockTestWindow", "A"))
        self.radioButton_2.setText(_translate("MockTestWindow", "B"))
        self.radioButton_3.setText(_translate("MockTestWindow", "C"))
        self.radioButton_4.setText(_translate("MockTestWindow", "D"))
        self.pushButton.setText(_translate("MockTestWindow", "上一题"))
        self.pushButton_2.setText(_translate("MockTestWindow", "下一题"))
        self.pushButton_3.setText(_translate("MockTestWindow", "交卷"))
        self.checkBox.setText(_translate("MockTestWindow", "A"))
        self.checkBox_2.setText(_translate("MockTestWindow", "B"))
        self.checkBox_3.setText(_translate("MockTestWindow", "C"))
        self.checkBox_4.setText(_translate("MockTestWindow", "D"))
        self.radioButton_5.setText(_translate("MockTestWindow", "Y"))
        self.radioButton_6.setText(_translate("MockTestWindow", "N"))
        self.radioButton_7.setText(_translate("MockTestWindow", "RadioButton"))
