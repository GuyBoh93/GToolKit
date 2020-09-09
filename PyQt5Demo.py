from PyQt5 import QtWidgets, QtGui, QtCore 
import sys


class GUIDemo(QtWidgets.QDialog):
    def __init__(self, _parent=None):
        super(GUIDemo, self).__init__(_parent)
        self.setWindowTitle("Window Name")

        self.ConstructRootUI()

        self.show()

    def ConstructRootUI(self):
        self.rootlayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.rootlayout)

        _label = QtWidgets.QLabel("List of Configs")
        _label.setAlignment(QtCore.Qt.AlignCenter)
        self.rootlayout.addWidget(_label)

        scrollArea = QtWidgets.QScrollArea()
        scrollAreaContentWidget = QtWidgets.QWidget()
        scrollArea.setWidget(scrollAreaContentWidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setMinimumHeight(100)
        scrollArea.setMinimumWidth(300)
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(
            scrollAreaContentWidget)
        self.rootlayout.addWidget(scrollArea)
    




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UI = GUIDemo()

    sys.exit(app.exec_())