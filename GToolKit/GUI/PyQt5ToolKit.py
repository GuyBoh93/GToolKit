from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class GUIBase():
    def __init__(self):
        self.rootLayout = QtWidgets.QHBoxLayout()

    def __del__(self):
        DelLayout(self.rootLayout)

    def SetRootLayoutType(self, _layoutType):
        self.rootLayout = _layoutType

    def GetLayout(self):
        return self.rootLayout


class ScoleBox(GUIBase):
    pass


class Button(GUIBase):
    pass


class FindFolderFled(GUIBase):
    pass


class FindFile(GUIBase):
    pass


class ShowMessageBox(QtWidgets.QDialog):
    pass


class ShowWarningBox(QtWidgets.QDialog):
    pass


class ShowErrorBox(QtWidgets.QDialog):
    pass


def DelLayout(_layout):
    try:
        while _layout.count():
            child = _layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                DelLayout(child.layout())
    except:
        pass


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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")

        label = QtWidgets.QLabel("This is a PyQt5 window!")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(QtCore.Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # UI = GUIDemo()
    gui = MainWindow()
    gui.show()

    sys.exit(app.exec_())
