from PyQt5.QtWidgets import QWidget, QComboBox, QLineEdit, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QMouseEvent
from PyQt5.Qt import Qt

global classIds
classIds = ''


def show_text(function):
    def wrapped(self, *args, **kwargs):
        global classIds
        if self.vars["showTextLock"]:
            self.vars["showTextLock"] = False
            result = function(self, *args, **kwargs)
            items = self.get_selected()
            l = len(items)
            l_ = self.vars["listViewModel"].rowCount() - 1
            self.vars["listViewModel"].item(0).setCheckState(
                Qt.Checked if l == l_ else Qt.Unchecked if l == 0 else Qt.PartiallyChecked)
            self.vars["lineEdit"].setText(
                "(全选)" if l == l_ else "(无选择)" if l == 0 else ";".join((item.text() for item in items)))
            self.vars["showTextLock"] = True

            classIds = "" if l == 0 else ",".join((item.text().split('.')[0] for item in items))
            # print(classIds)
        else:
            result = function(self, *args, **kwargs)
        return result

    return wrapped


class QComboCheckBox(QComboBox):
    class MyListView(QListView):
        def __init__(self, parent: QWidget = None, vars=None):
            super().__init__(parent)
            self.vars = vars

        def mousePressEvent(self, event: QMouseEvent):
            self.vars["lock"] = False
            super().mousePressEvent(event)

        def mouseDoubleClickEvent(self, event: QMouseEvent):
            self.vars["lock"] = False
            super().mouseDoubleClickEvent(event)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.vars = dict()
        self.vars["lock"] = True
        self.vars["showTextLock"] = True
        # 装饰器锁，避免批量操作时重复改变lineEdit的显示
        self.vars["lineEdit"] = QLineEdit(self)
        self.vars["lineEdit"].setReadOnly(True)
        self.vars["listView"] = self.MyListView(self, self.vars)
        self.vars["listViewModel"] = QStandardItemModel(self)
        self.setModel(self.vars["listViewModel"])
        self.setView(self.vars["listView"])
        self.setLineEdit(self.vars["lineEdit"])

        self.activated.connect(self.__show_selected)

        self.add_item("(全选)")

    def count(self):
        # 返回子项数
        return super().count() - 1

    @show_text
    def add_item(self, text: "str", flag=False):
        # 根据文本添加子项
        item = QStandardItem()
        item.setText(text)
        item.setCheckable(True)
        if flag:
            item.setCheckState(Qt.Checked)
        self.vars["listViewModel"].appendRow(item)

    @show_text
    def add_items(self, texts: "tuple or list"):
        # 根据文本列表添加子项
        for text in texts:
            self.add_item(text)

    @show_text
    def clear_items(self):
        # 清空所有子项
        self.vars["listViewModel"].clear()
        self.add_item("(全选)")

    def find_index(self, index: "int"):
        # 根据索引查找子项
        return self.vars["listViewModel"].item(index if index < 0 else index + 1)

    def find_indexs(self, indexs: "tuple or list"):
        # 根据索引列表查找子项
        return [self.find_index(index) for index in indexs]

    def find_text(self, text: "str"):
        # 根据文本查找子项
        tempList = self.vars["listViewModel"].findItems(text)
        tempList.pop(0) if tempList and tempList[0].row() == 0 else tempList
        return tempList

    def find_texts(self, texts: "tuple or list"):
        # 根据文本列表查找子项
        return {text: self.find_text(text) for text in texts}

    def get_class_text(self):
        # 获取班级ids
        return classIds

    def get_text(self, index: "int"):
        # 根据索引返回文本
        return self.vars["listViewModel"].item(index if index < 0 else index + 1).text()

    def get_texts(self, indexs: "tuple or list"):
        # 根据索引列表返回文本
        return [self.get_text(index) for index in indexs]

    def change_text(self, index: "int", text: "str"):
        # 根据索引改变某一子项的文本
        self.vars["listViewModel"].item(index if index < 0 else index + 1).setText(text)

    @show_text
    def select_index(self, index: "int", state: "bool" = True):
        # 根据索引选中子项，state=False时为取消选中
        self.vars["listViewModel"].item(index if index < 0 else index + 1).setCheckState(
            Qt.Checked if state else Qt.Unchecked)

    @show_text
    def select_indexs(self, indexs: "tuple or list", state: "bool" = True):
        # 根据索引列表选中子项，state=False时为取消选中
        for index in indexs:
            self.select_index(index, state)

    @show_text
    def select_text(self, text: "str", state: "bool" = True):
        # 根据文本选中子项，state=False时为取消选中
        for item in self.find_text(text):
            item.setCheckState(Qt.Checked if state else Qt.Unchecked)

    @show_text
    def select_texts(self, texts: "tuple or list", state: "bool" = True):
        # 根据文本列表选中子项，state=False时为取消选中
        for text in texts:
            self.select_text(text, state)

    @show_text
    def select_reverse(self):
        # 反转选择
        if self.vars["listViewModel"].item(0).checkState() == Qt.Unchecked:
            self.select_all()
        elif self.vars["listViewModel"].item(0).checkState() == Qt.Checked:
            self.select_clear()
        else:
            for row in range(1, self.vars["listViewModel"].rowCount()):
                self.__select_reverse(row)

    def __select_reverse(self, row: "int"):
        item = self.vars["listViewModel"].item(row)
        item.setCheckState(Qt.Unchecked if item.checkState() == Qt.Checked else Qt.Checked)

    @show_text
    def select_all(self):
        # 全选
        for row in range(0, self.vars["listViewModel"].rowCount()):
            self.vars["listViewModel"].item(row).setCheckState(Qt.Checked)

    @show_text
    def select_clear(self):
        # 全不选
        for row in range(0, self.vars["listViewModel"].rowCount()):
            self.vars["listViewModel"].item(row).setCheckState(Qt.Unchecked)

    @show_text
    def remove_index(self, index: "int"):
        # 根据索引移除子项
        return self.vars["listViewModel"].takeRow(index if index < 0 else index + 1)

    @show_text
    def remove_indexs(self, indexs: "tuple or list"):
        # 根据索引列表移除子项
        return [self.remove_index(index) for index in sorted(indexs, reverse=True)]

    @show_text
    def remove_text(self, text: "str"):
        # 根据文本移除子项
        items = self.find_text(text)
        indexs = [item.row() for item in items]
        return [self.vars["listViewModel"].takeRow(index) for index in sorted(indexs, reverse=True)]

    @show_text
    def remove_texts(self, texts: "tuple or list"):
        # 根据文本列表移除子项
        return {text: self.remove_text(text) for text in texts}

    def get_selected(self):
        # 获取当前选择的子项
        items = list()
        for row in range(1, self.vars["listViewModel"].rowCount()):
            item = self.vars["listViewModel"].item(row)
            if item.checkState() == Qt.Checked:
                items.append(item)
        return items

    def is_all(self):
        # 判断是否是全选
        return True if self.vars["listViewModel"].item(0).checkState() == Qt.Checked else False

    def sort(self, order=Qt.AscendingOrder):
        # 排序，默认正序
        self.vars["listViewModel"].sort(0, order)

    @show_text
    def __show_selected(self, index):
        if not self.vars["lock"]:
            if index == 0:
                if self.vars["listViewModel"].item(0).checkState() == Qt.Checked:
                    self.select_clear()
                else:
                    self.select_all()
            else:
                self.__select_reverse(index)

            self.vars["lock"] = True

    def hidePopup(self):
        if self.vars["lock"]:
            super().hidePopup()
