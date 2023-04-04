from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtCore


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)

        # self.lineEdit.returnPressed.connect(self.add_item)

        self.select_button.clicked.connect(self.select_all)
        self.unselect_button.clicked.connect(self.unselect_all)
        self.add_button.clicked.connect(self.add_item)
        self.finish_button.clicked.connect(self.remove_item)

    def remove_item(self):
        for i in reversed(range(self.todo_listWidget.count())):
            item = self.todo_listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                self.todo_listWidget.takeItem(i)

    def select_all(self):
        for i in range(self.todo_listWidget.count()):
            item = self.todo_listWidget.item(i)
            if item.checkState() == QtCore.Qt.Unchecked:
                item.setCheckState(QtCore.Qt.Checked)

    def unselect_all(self):
        for i in range(self.todo_listWidget.count()):
            item = self.todo_listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)

    def add_item(self):
        line_text = self.lineEdit.text()
        if line_text:
            new_item = QListWidgetItem(line_text)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsUserCheckable)
            new_item.setCheckState(QtCore.Qt.Unchecked)
            self.todo_listWidget.addItem(new_item)
            self.lineEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
