# Table of Contents

- [Examples](#Examples)
    - [Json Management](#Json-Management)
    - [GUI](#GUI)


# Examples 
## Json Management
```python
from GToolKit.Json import JsonToolKit

# get Json in a Path
from GToolKit.Json import JsonToolKit

locationOfJson = "C:\scripts"

# get Json in a Path
paths = JsonToolKit.GetAllJsonPaths(locationOfJson)
# or
paths = JsonToolKit.GetAllJsonPathsCalled(locationOfJson, "Testjson")


# Opeing all the json so Python can Read them
dicts = []
for path in paths:
    dict = JsonToolKit.GetJsonAsDict(path)
    dict['New Key'] = "New Value"
    dicts.append(dict)
    print


# Saveing new Data to Json
for i, path in paths:
    JsonToolKit.SaveDictToJsonFullPath(path, dicts[i])
```

## GUI 
Basic GUI Setting Up a Float Input Only
```python
from GToolKit.Json import GUIFromDict
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MainWindow(QtWidgets.QDialog):
    def __init__(self, _parent=None):
        super(MainWindow, self).__init__(_parent)
        self.rootlayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.rootlayout)
        
        
        self.floatGUI = GUIFromDict.FloatInputUI("Key", 3, self) 
        self.rootlayout.addLayout(self.floatGUI.GetGUILayout())

        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()

    sys.exit(app.exec_())
```