# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit

from grade_statistics.src.utils.ComboCheckBox import QComboCheckBox
from grade_statistics.src.vals.db import sql_execute
from grade_statistics.src.vals.sqls import *


class AddAdmin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 279)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QLineEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 30, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.label0 = QtWidgets.QLabel(Form)
        self.label0.setGeometry(QtCore.QRect(40, 90, 54, 12))
        self.label0.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label0.setObjectName("label")
        self.textEdit0 = QtWidgets.QLineEdit(Form)
        self.textEdit0.setGeometry(QtCore.QRect(100, 80, 181, 31))
        self.textEdit0.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 130, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 54, 12))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        classlist = sql_execute(getClassList('0', ''))
        self.textEdit_3 = QComboCheckBox(Form)
        for class_ in classlist:
            self.textEdit_3.add_item('%d.%s' % (class_[0], class_[1]), flag=False)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 180, 181, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(23, 190, 71, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.addAdmin(Form))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: Form.hide())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????????"))
        self.label.setText(_translate("Form", "????????????"))
        self.label0.setText(_translate("Form", "?????????"))
        self.label_2.setText(_translate("Form", "?????????"))
        self.label_3.setText(_translate("Form", "??????????????????"))
        self.pushButton.setText(_translate("Form", "??????"))
        self.pushButton_2.setText(_translate("Form", "??????"))

    def addAdmin(self, Form):
        username = self.textEdit.text()
        passw = self.textEdit0.text()
        mark = self.textEdit_2.text()
        classids = self.textEdit_3.get_class_text()
        sql_execute(insertAdmin(username, passw, mark, classids))
        QMessageBox.about(Form, '??????', "?????????????????????????????????????????????")
        Form.hide()

if __name__ == "__main__":
    import sys

    App = QApplication(sys.argv)  # ??????QApplication???????????????GUI???????????????
    aw = AddAdmin()  # ?????????????????????????????????Ui_MainWindow
    w = QMainWindow()  # ?????????QMainWindow???
    aw.setupUi(w)  # ?????????????????????setupUi????????????QMainWindow??????????????????
    w.show()  # ???????????????
    w.setWindowTitle('????????????')
    sys.exit(App.exec_())  # ???????????????????????????
