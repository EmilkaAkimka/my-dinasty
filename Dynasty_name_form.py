# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dynasty_name_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dynasty_name_form(object):
    def setupUi(self, dynasty_name_form):
        dynasty_name_form.setObjectName("dynasty_name_form")
        dynasty_name_form.resize(1073, 400)
        dynasty_name_form.setMaximumSize(QtCore.QSize(1073, 400))
        self.label = QtWidgets.QLabel(dynasty_name_form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1141, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("5196-4V-1_Wood-Texture.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dynasty_name_form)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 971, 81))
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(dynasty_name_form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 160, 611, 71))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(dynasty_name_form)
        self.pushButton.setGeometry(QtCore.QRect(620, 260, 191, 61))
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dynasty_name_form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 191, 61))
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dynasty_name_form)
        QtCore.QMetaObject.connectSlotsByName(dynasty_name_form)

    def retranslateUi(self, dynasty_name_form):
        _translate = QtCore.QCoreApplication.translate
        dynasty_name_form.setWindowTitle(_translate("dynasty_name_form", "Dynasty name form"))
        self.label_2.setText(_translate("dynasty_name_form", "Here begins the path of your dinasty,chose the name of your dynasty"))
        self.pushButton.setText(_translate("dynasty_name_form", "ACCEPT"))
        self.pushButton_2.setText(_translate("dynasty_name_form", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dynasty_name_form = QtWidgets.QWidget()
    ui = Ui_dynasty_name_form()
    ui.setupUi(dynasty_name_form)
    dynasty_name_form.show()
    sys.exit(app.exec_())
