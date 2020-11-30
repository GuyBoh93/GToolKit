from GUIFromDict import DictToWidgetElement
from PyQt5 import QtWidgets
import sys


class MainWindow(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Test Window")

        widget = DictToWidgetElement("Test", dictx)
        print(widget.GetValue())

        self.rootLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.rootLayout)
        self.rootLayout.addLayout(widget.GetGUILayout())

        

        self.show()


if __name__ == "__main__":

    dictx = {"Abc": 1}

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()

    app.exec_()
