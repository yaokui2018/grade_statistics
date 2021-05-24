# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):  # 图形界面类
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 150)
        # 文本框
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 100, 28))  # x坐标,y坐标,宽,高
        self.lineEdit.setObjectName("lineEdit")
        # 按钮
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 100, 28))
        self.pushButton.setObjectName("pushButton")
        # 标签
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 100, 100, 28))
        self.label.setObjectName("label")

        self.retranslateUi(Form)

    def retranslateUi(self, Form):  # 设置各组件的文本
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "这是一个测试窗口"))
        self.pushButton.setText(_translate("Form", "测试按钮"))
        self.label.setText(_translate("Form", "原文字"))


# 以上是图形界面代码，不用手写。可以用Qt Designer定制，然后用pyuic生成。
#
# ui转py命令：  python -m PyQt5.uic.pyuic xxx.ui -o xxx_ui.py
#
##################################################################


# from PyQt5 import QtWidgets                       # 上面ui部分已经调用过了，这里就先注释掉
# from myUi import Ui_Form                          # 界面类、逻辑类分离的话，myUi的名字就是ui文件名

# class MyWindow(QtWidgets.QWidget, Ui_Form):  # 括号中的Ui_Form要跟ui.py文件里的class同名
#     def __init__(self, parent=None):
#         super(MyWindow, self).__init__(parent)
#         self.setupUi(self)  # 生成界面
#         QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))  # 界面风格
#
#         self.pushButton.clicked.connect(self.btn_clicked)  # 按钮信号槽      ################ 按需修改
#
#         self.setGeometry(300, 300, 1200, 600)
#         self.setWindowTitle('管理员登录 - 小学生成绩管理系统')
#
#     def btn_clicked(self):  # 槽函数       ################ 按需修改
#         input_words = self.lineEdit.text()
#         self.label.setText(input_words)
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = MyWindow()
#     myshow.show()
#     sys.exit(app.exec_())


# -*- encoding: utf-8 -*-
'''
@Contact :   obj2008@foxmail.com
2020/5/13 12:48 PM   obj2008      1.0         None
--------------------------------------------------------
'''
# import sys
#
# from PyQt5.QtWidgets import QApplication, QWidget,  QVBoxLayout,  QTableWidget, QCheckBox, QHeaderView, QStyle, QStyleOptionButton, QTableWidgetItem
# from PyQt5.QtCore import Qt, pyqtSignal, QRect
#
# # 表头字段，全局变量
# header_field = ['全选', '姓名', '年龄', '籍贯']
# # 用来装行表头所有复选框 全局变量
# all_header_combobox = []
#
#
# class CheckBoxHeader(QHeaderView):
#     """自定义表头类"""
#
#     # 自定义 复选框全选信号
#     select_all_clicked = pyqtSignal(bool)
#     # 这4个变量控制列头复选框的样式，位置以及大小
#     _x_offset = 0
#     _y_offset = 0
#     _width = 20
#     _height = 20
#
#     def __init__(self, orientation=Qt.Horizontal, parent=None):
#         super(CheckBoxHeader, self).__init__(orientation, parent)
#         self.isOn = False
#
#     def paintSection(self, painter, rect, logicalIndex):
#         painter.save()
#         super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
#         painter.restore()
#
#         self._y_offset = int((rect.height() - self._width) / 2.)
#
#         if logicalIndex == 0:
#             option = QStyleOptionButton()
#             option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
#             option.state = QStyle.State_Enabled | QStyle.State_Active
#             if self.isOn:
#                 option.state |= QStyle.State_On
#             else:
#                 option.state |= QStyle.State_Off
#             self.style().drawControl(QStyle.CE_CheckBox, option, painter)
#
#     def mousePressEvent(self, event):
#         index = self.logicalIndexAt(event.pos())
#         if 0 == index:
#             x = self.sectionPosition(index)
#             if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
#                 if self.isOn:
#                     self.isOn = False
#                 else:
#                     self.isOn = True
#                     # 当用户点击了行表头复选框，发射 自定义信号 select_all_clicked()
#                 self.select_all_clicked.emit(self.isOn)
#
#                 self.updateSection(0)
#         super(CheckBoxHeader, self).mousePressEvent(event)
#
#     # 自定义信号 select_all_clicked 的槽方法
#     def change_state(self, isOn):
#         # 如果行表头复选框为勾选状态
#         if isOn:
#             # 将所有的复选框都设为勾选状态
#             for i in all_header_combobox:
#                 i.setCheckState(Qt.Checked)
#         else:
#             for i in all_header_combobox:
#                 i.setCheckState(Qt.Unchecked)
#
#
# class TableDemo(QWidget):
#     """窗口类"""
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('这是QTableWidget类行表头添加复选框全选功能')
#         self.resize(400, 300)
#
#         # 垂直布局
#         self.vlayout = QVBoxLayout(self)
#         self.vlayout.setAlignment(Qt.AlignTop)  # 设置 垂直布局 的对齐方式
#         self.setTableWidget()  # 设置表格
#
#         self.show()
#
#     # 设置表格
#     def setTableWidget(self):
#         # 表格控件
#         self.tablewidget = QTableWidget(3,4)        # 3行4列
#         self.tablewidget.setFixedWidth(300)         # 表格宽度
#         self.setTableHeaderField()               # 设置表格行表头字段
#         self.tablewidget.setAlternatingRowColors(True)      # 交替行颜色
#         self.vlayout.addWidget(self.tablewidget)
#
#     # 设置行表头字段
#     def setTableHeaderField(self):
#
#         self.tablewidget.setColumnCount(len(header_field))   # 设置列数
#         for i in range(len(header_field)-1):
#             header_item = QTableWidgetItem(header_field[i])
#
#             checkbox = QCheckBox()
#             # 将所有的复选框都添加到 全局变量 all_header_combobox 中
#             all_header_combobox.append(checkbox)
#             # 为每一行添加复选框
#             self.tablewidget.setCellWidget(i,0,checkbox)
#
#         header = CheckBoxHeader()               # 实例化自定义表头
#         self.tablewidget.setHorizontalHeader(header)            # 设置表头
#         self.tablewidget.setHorizontalHeaderLabels(header_field)        # 设置行表头字段
#         self.tablewidget.setColumnWidth(0,60)       # 设置第0列宽度
#         header.select_all_clicked.connect(header.change_state)        # 行表头复选框单击信号与槽
#
#     # 设置表格内容，根据实际情况设置即可
#     def setTableContents(self):
#         pass
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ta = TableDemo()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtWidgets import QTableWidget
# from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtWidgets import QAbstractItemView
# from PyQt5.QtWidgets import QPushButton
# from qtpy.QtCore import Qt
#
#
# class testWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.table = QTableWidget(self)
#         self.table.move(20, 20)
#         self.table.setColumnCount(3)
#         self.table.setFixedHeight(300)
#         self.table.setFixedWidth(500)
#         self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置表格的选取方式是行选取
#         self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选取方式为单个选取
#         self.table.setHorizontalHeaderLabels(["标记ID", "标记名称", "标记初始坐标"])  # 设置行表头
#         self.table.verticalHeader().setVisible(False)  # 隐藏列表头
#
#         self.table_insert()
#
#         self.table.itemChanged.connect(self.table_update)
#
#         self.delete_button = QPushButton(self)
#         self.delete_button.move(230, 350)
#         self.delete_button.setFixedWidth(100)
#         self.delete_button.setFixedHeight(32)
#         self.delete_button.clicked.connect(self.table_delete)
#         self.delete_button.setText("Delete")
#
#         self.setGeometry(200, 200, 570, 400)
#         self.show()
#
#     # insert,只是简单插入一个固定数据
#     def table_insert(self):
#         row = self.table.rowCount()
#         self.table.insertRow(row)
#
#         item_id = QTableWidgetItem("1")
#         item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择（未设置可编辑）
#
#         item_name = QTableWidgetItem("door")  # 我们要求它可以修改，所以使用默认的状态即可
#
#         item_pos = QTableWidgetItem("(1,2)")
#         item_pos.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # 设置物件的状态为只可被选择
#
#         self.table.setItem(row, 0, item_id)
#         self.table.setItem(row, 1, item_name)
#         self.table.setItem(row, 2, item_pos)
#         # 以下可以加入保存数据到数据的操作
#
#     # update
#     def table_update(self):
#         row_select = self.table.selectedItems()
#         if len(row_select) == 0:
#             return
#         id = row_select[0].text()
#         new_name = row_select[1].text()
#         print("id: {}, save_name: {}".format(id, new_name))
#         # 以下可以加入保存数据到数据的操作
#         '''
#         eg. update {table} set name = "new_name" where id = "id"
#         '''
#
#     # delete
#     def table_delete(self):
#         row_select = self.table.selectedItems()
#         if len(row_select) == 0:
#             return
#         id = row_select[0].text()
#         print("id: {}".format(id))
#
#         row = row_select[0].row()
#         self.table.removeRow(row)
#         # 以下可以加入保存数据到数据的操作
#         '''
#         eg. delete from {table} where id = "id"
#         '''
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = testWindow()
#     sys.exit(app.exec_())

from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidget, QCheckBox, QListWidgetItem, QApplication
from PyQt5.QtCore import pyqtSignal
import sys

"""
1.将show函数改成show0
2.增加changeitemlist函数
3.增加信号signa
"""


class ComboCheckBox(QComboBox):
    signa = pyqtSignal(list)

    def __init__(self, items):  # items==[str,str...]
        super(ComboCheckBox, self).__init__()
        self.items = items
        self.items.insert(0, '全部')

        self.row_num = len(self.items)
        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show0)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)
        self.setMaxVisibleItems(100)  # 避免滑条的出现引起滑条偷吃标签的问题

    def addQCheckBox(self, i):
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.items[i])
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])

    def Selectlist(self):
        Outputlist = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        self.Selectedrow_num = len(Outputlist)

        return Outputlist

    def show0(self):
        show0 = ''
        Outputlist = self.Selectlist()
        self.signa.emit(Outputlist)
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show0 += i + ';'
        if self.Selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(0)
        elif self.Selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(2)
        else:
            self.qCheckBox[0].setCheckState(1)
        self.qLineEdit.setText(show0)
        self.qLineEdit.setReadOnly(True)

    def All(self, zhuangtai):
        if zhuangtai == 2:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif zhuangtai == 1:
            if self.Selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(2)
        elif zhuangtai == 0:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)

    def changeitemlist(self, itemlist):

        self.items = itemlist
        self.items.insert(0, '全部')
        self.row_num = len(self.items)

        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show0)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ComboCheckBox(['装置ID', '传感器ID', "采样时间", '装置电源电压', "信号强度",'装置ID', '传感器ID', "采样时间", '装置电源电压', "信号强度"])
    def solt11(x):
        print(x)
    mainWindow.signa.connect(solt11)
    mainWindow.show()
    sys.exit(app.exec_())

