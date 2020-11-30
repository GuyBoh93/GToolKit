import json
import os
from PyQt5 import QtWidgets, QtGui
import ntpath
import JsonToolKit


class jsonBase():
    def __init__(self, _key, _value, _parent, _useGroupBox=False, SetLayoutVertical=False, _backgroundColourIndex=0):
        if SetLayoutVertical:
            self.baseLayout = QtWidgets.QVBoxLayout()
        else:
            self.baseLayout = QtWidgets.QHBoxLayout()
        self.value = _value
        self.key = _key

        self.useGroupBox = _useGroupBox
        self.backGroundColourIndex = _backgroundColourIndex
        self.SetDesign()

        self.parent = _parent

    def __del__(self):
        try:
            DelLayout(self.baseLayout)
        except:
            pass
        if self.useGroupBox:
            DelLayout(self.rootLayout)

    def SetDesign(self):
        if self.useGroupBox:
            # self.baseLayout.addStretch(10)
            self.group = QtWidgets.QGroupBox()
            self.group.setLayout(self.baseLayout)
            self.group.setTitle(self.key)
            if self.backGroundColourIndex == 1:
                self.group.setStyleSheet("QGroupBox { \
                                        padding-top: 20px; \
                                        border-radius: 9px; \
                                        border: 2px solid rgb(0, 0, 0); \
                                        background-color: rgb(200, 200, 200)}")
            elif self.backGroundColourIndex == 2:
                pass
            else:
                if self.backGroundColourIndex == 1:
                    self.group.setStyleSheet("QGroupBox { \
                                        padding-top: 20px; \
                                        border-radius: 9px; \
                                        border: 2px solid rgb(0, 0, 0); }")

            self.rootLayout = QtWidgets.QHBoxLayout()
            self.rootLayout.addWidget(self.group)
        else:
            self.label = QtWidgets.QLabel(str(self.key))
            self.baseLayout.addWidget(self.label)

    def GetKey(self):
        return self.key

    def GetValue(self):
        return self.value

    def GetGUILayout(self):
        if self.useGroupBox:
            return self.rootLayout
        else:
            return self.baseLayout

    def SetValue(self, _value):
        self.value = _value


class FloatInputUI(jsonBase):
    def __init__(self, _key, _value, _parent):
        # Convertions
        _key = str(_key)
        _value = float(_value)

        # Storing Vars
        self.parent = _parent
        jsonBase.__init__(self, _key, _value, _parent)

        # UI
        self.MakeUI()

    def MakeUI(self):
        self.floatLineEdit = QtWidgets.QLineEdit(str(self.value))
        _onlyFloat = QtGui.QDoubleValidator()
        self.floatLineEdit.setValidator(
            _onlyFloat)  # Set only float inputs only
        self.floatLineEdit.textChanged.connect(self.InputChanged)
        self.baseLayout.addWidget(self.floatLineEdit)

    def InputChanged(self, _input):
        self.SetValue(float(_input))

    def SetValue(self, _value):
        jsonBase.SetValue(self, float(_value))
        self.floatLineEdit.setText(str(self.value))


class StringInputUI(jsonBase):
    def __init__(self, _key, _value, _parent):
        # convertions
        _key = str(_key)
        _value = str(_value)
        # Init Values
        jsonBase.__init__(self, _key, _value, _parent)
        # UI
        self.MakeUI()

    def MakeUI(self):
        self.stringLineEdit = QtWidgets.QLineEdit(str(self.value))
        self.stringLineEdit.textChanged.connect(self.InputChanged)
        self.baseLayout.addWidget(self.stringLineEdit)

    def InputChanged(self, _input):
        self.SetValue(str(_input))

    def SetValue(self, _value):
        jsonBase.SetValue(self, str(_value))
        self.stringLineEdit.setText(str(self.value))


class BoolInputUI(jsonBase):
    def __init__(self, _key, _value, _parent):
        # Convertions
        _key = str(_key)
        _value = bool(_value)
        # Init Vars
        jsonBase.__init__(self, _key, _value, _parent)
        # UI
        self.MakeUI()

    def MakeUI(self):
        self.boolCheckBox = QtWidgets.QCheckBox("")
        self.boolCheckBox.setChecked(self.value)
        self.boolCheckBox.stateChanged.connect(self.InputChanged)
        self.baseLayout.addWidget(self.boolCheckBox)

    def InputChanged(self, _input):
        self.SetValue(bool(_input))

    def SetValue(self, _value):
        jsonBase.SetValue(self, bool(_value))
        self.boolCheckBox.setChecked(bool(self.value))


class ArrayInputUI(jsonBase):
    def __init__(self, _key, _value, _parent):
        _key = str(_key)
        _value = list(_value)
        jsonBase.__init__(self, _key, _value, _parent, True)
        self.childObjects = []
        self.MakeUI()

    def __del__(self):
        for _key in self.childObjects:
            try:
                self.childObjects[_key].__del__()
            except:
                pass
        jsonBase.__del__(self)

    def MakeUI(self):
        self.vertLayout = QtWidgets.QVBoxLayout()
        _label = QtWidgets.QLabel(str(self.key))
        self.vertLayout.addWidget(_label)

        self.addtypeCB = QtWidgets.QComboBox()
        self.addtypeCB.addItem("String")
        self.addtypeCB.addItem("float")
        self.addtypeCB.addItem("bool")
        # self.addtypeCB.currentIndexChanged.connect(self.TypeToAddChanged)
        self.baseLayout.addWidget(self.addtypeCB)
        # Buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.minuseButton = QtWidgets.QPushButton("-")
        self.minuseButton.clicked.connect(self.RemoveElement)
        self.plusButton = QtWidgets.QPushButton("+")
        self.plusButton.clicked.connect(self.AddElement)
        self.buttonLayout.addWidget(self.minuseButton)
        self.buttonLayout.addWidget(self.plusButton)
        self.vertLayout.addLayout(self.buttonLayout)
        self.baseLayout.addLayout(self.vertLayout)

        ###Scrole ###
        self.scrollArea = QtWidgets.QScrollArea()
        self.contentWidget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.contentWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumHeight(100)
        self.scrollArea.setMinimumWidth(200)
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.contentWidget)
        self.baseLayout.addWidget(self.scrollArea)

        self.PopulatesInputsWithList()

    def PopulatesInputsWithList(self):
        for _child in self.childObjects:
            _child.__del__()
            del _child
        self.childObjects.clear()

        index = 0
        for _value in self.value:
            if isinstance(_value, dict):
                if IsVector(_value):
                    _obj = JsonStrut(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)
                else:
                    _obj = JsonStrut(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)
            else:
                if isinstance(_value, bool):
                    _obj = BoolInputUI(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)
                elif isinstance(_value, float) or isinstance(_value, int):
                    _obj = FloatInputUI(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)
                elif isinstance(_value, str):
                    _obj = StringInputUI(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)
                elif isinstance(_value, list):
                    _obj = ArrayInputUI(str(index), _value, self)
                    self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
                    self.childObjects.append(_obj)

                else:
                    print("Can not Sort this: " + _value)
            index += 1

    def AddElement(self):
        index = len(self.childObjects)

        if self.addtypeCB.currentText() == "String":
            _obj = StringInputUI(str(index), "", self)
            self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
            self.childObjects.append(_obj)

        elif self.addtypeCB.currentText() == "float":
            _obj = FloatInputUI(str(index), 0, self)
            self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
            self.childObjects.append(_obj)

        elif self.addtypeCB.currentText() == "bool":
            _obj = BoolInputUI(str(index), False, self)
            self.scrollAreaLayout.addLayout(_obj.GetGUILayout())
            self.childObjects.append(_obj)

    def RemoveElement(self):
        _arrayLength = len(self.childObjects)
        if _arrayLength-1 >= 0:
            self.childObjects[_arrayLength-1].__del__()
            del self.childObjects[_arrayLength-1]

        _targetValue = []
        for _childObject in self.childObjects:
            _targetValue.append(_childObject.GetValue())
        self.SetValue(_targetValue)

    def ChildChangedValue(self, _child):
        _targetValue = []
        for _child in self.childObjects:
            _targetValue.append(_child.GetValue())
        jsonBase.SetValue(self, _targetValue)

    def SetValue(self, _value):
        self.value.clear()
        print("!!!!!!!!!!!!")
        jsonBase.SetValue(self, _value)
        self.PopulatesInputsWithList()

    def GetValue(self):
        _updatedValues = []
        for _child in self.childObjects:
            _updatedValues.append(_child.GetValue())
        jsonBase.SetValue(self, _updatedValues)

        return jsonBase.GetValue(self)


class JsonStrut(jsonBase):
    def __init__(self, _key, _value, _parent):
        # convertions
        _key = str(_key)
        _value = _value
        # Init Vars
        jsonBase.__init__(self, _key, _value, _parent, True, True)
        self.childObjects = {}
        # UI
        self.MakeUI()
        # self.baseLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

    def __del__(self):
        for _child in self.childObjects:
            try:
                _child.__del__()
            except:
                pass
        jsonBase.__del__(self)

    def MakeUI(self):
        for key in self.value:
            if isinstance(self.value[key], dict):
                if IsVector(self.value[key]):
                    self.childObjects[key] = JsonStrut(
                        key, self.value[key], self)
                else:
                    self.childObjects[key] = JsonStrut(
                        key, self.value[key], self)
            else:
                if isinstance(self.value[key], bool):
                    self.childObjects[key] = BoolInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], float) or isinstance(self.value[key], int):
                    self.childObjects[key] = FloatInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], str):
                    self.childObjects[key] = StringInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], list):
                    self.childObjects[key] = ArrayInputUI(
                        key, self.value[key], self)
                else:
                    print("Can not Sort this: " + self.value[key])
            self.baseLayout.addLayout(self.childObjects[key].GetGUILayout())

    def ChildChangedValue(self, _child):
        _targetValue = self.GetValue()
        _targetValue[_child.GetKey()] = _child.GetValue()
        self.SetValue(_targetValue)

    def SetValue(self, _value):
        jsonBase.SetValue(self, _value)

        for _child in self.childObjects:
            self.childObjects[_child].SetValue(
                _value[self.childObjects[_child].GetKey()])

    def GetValue(self):
        _updatedValues = {}
        for _child in self.childObjects:
            _updatedValues[_child] = self.childObjects[_child].GetValue()

        jsonBase.SetValue(self, _updatedValues)
        return jsonBase.GetValue(self)


class JsonToGUIElement(jsonBase):
    def __init__(self, _jsonLocation):
        self.jsonLocation = _jsonLocation
        _value = JsonToolKit.GetJsonAsDict(self.jsonLocation)
        _key = str(ntpath.basename(_jsonLocation))
        jsonBase.__init__(self, _key, _value, self, True, True, 1)

        self.ChildObjects = {}
        self.MakeUI()

    def MakeUI(self):
        for key in self.value:
            if isinstance(self.value[key], dict):
                if IsVector(self.value[key]):
                    self.ChildObjects[key] = JsonStrut(
                        key, self.value[key], self)
                else:
                    self.ChildObjects[key] = JsonStrut(
                        key, self.value[key], self)
            else:
                if isinstance(self.value[key], bool):
                    self.ChildObjects[key] = BoolInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], float) or isinstance(self.value[key], int):
                    self.ChildObjects[key] = FloatInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], str):
                    self.ChildObjects[key] = StringInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], list):
                    self.ChildObjects[key] = ArrayInputUI(
                        key, self.value[key], self)
                else:
                    print("Can not Sort this: " + self.value[key])
            self.baseLayout.addLayout(self.ChildObjects[key].GetGUILayout())

    def GetValuesFromUIElementsToValue(self):
        for key in self.ChildObjects:
            if isinstance(self.ChildObjects[key], BoolInputUI):
                self.value[key] = bool(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], JsonStrut):
                self.value[key] = self.ChildObjects[key].GetValue()
            elif isinstance(self.ChildObjects[key], JsonStrut):
                self.value[key] = self.ChildObjects[key].GetValue()
            elif isinstance(self.ChildObjects[key], FloatInputUI):
                self.value[key] = float(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], StringInputUI):
                self.value[key] = str(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], ArrayInputUI):
                # self.ChildObjects[key].SetValue()
                self.value[key] = list(self.ChildObjects[key].GetValue())
            else:
                pass

    # Updates All existing UI With With new json With the same name. Just pass though the new folder Location
    def UpdateCurrentUIWithNewJsonValuse(self, _folderPath):

        _newJsonPath = _folderPath + os.sep + self.GetKey()
        if os.path.exists(_newJsonPath):
            # remove current settings
            for _key in self.ChildObjects:
                self.ChildObjects[_key].__del__()

            self.ChildObjects.clear()

            _newData = JsonToolKit.GetJsonAsDict(_newJsonPath)
            self.SetValue(_newData)

            self.MakeUI()
        else:
            print("Json File Does Not exist: ", self.GetKey())

    def SaveJson(self, _path):
        _location = _path
        _name = self.key
        self.GetValuesFromUIElementsToValue()
        JsonToolKit.SaveDictToJson(_location, _name, self.value)


class DictToWidgetElement(jsonBase):
    def __init__(self, _name, _dict):
        self.jsonLocation = _dict
        _value = _dict
        _key = _name
        jsonBase.__init__(self, _key, _value, self, True, True, 1)

        self.ChildObjects = {}
        self.MakeUI()
        print (len(self.ChildObjects))

    def MakeUI(self):
        for key in self.value:
            if isinstance(self.value[key], dict):
                if IsVector(self.value[key]):
                    self.ChildObjects[key] = JsonStrut(
                        key, self.value[key], self)
                else:
                    self.ChildObjects[key] = JsonStrut(
                        key, self.value[key], self)
            else:
                if isinstance(self.value[key], bool):
                    self.ChildObjects[key] = BoolInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], float) or isinstance(self.value[key], int):
                    self.ChildObjects[key] = FloatInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], str):
                    self.ChildObjects[key] = StringInputUI(
                        key, self.value[key], self)
                elif isinstance(self.value[key], list):
                    self.ChildObjects[key] = ArrayInputUI(
                        key, self.value[key], self)
                else:
                    print("Can not Sort this: " + self.value[key])
            self.baseLayout.addLayout(self.ChildObjects[key].GetGUILayout())

    def GetValuesFromUIElementsToValue(self):
        for key in self.ChildObjects:
            if isinstance(self.ChildObjects[key], BoolInputUI):
                self.value[key] = bool(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], JsonStrut):
                self.value[key] = self.ChildObjects[key].GetValue()
            elif isinstance(self.ChildObjects[key], JsonStrut):
                self.value[key] = self.ChildObjects[key].GetValue()
            elif isinstance(self.ChildObjects[key], FloatInputUI):
                self.value[key] = float(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], StringInputUI):
                self.value[key] = str(self.ChildObjects[key].GetValue())
            elif isinstance(self.ChildObjects[key], ArrayInputUI):
                # self.ChildObjects[key].SetValue()
                self.value[key] = list(self.ChildObjects[key].GetValue())
            else:
                pass

    # Updates All existing UI With With new json With the same name. Just pass though the new folder Location
    def UpdateCurrentUIWithNewJsonValuse(self, _folderPath):

        _newJsonPath = _folderPath + os.sep + self.GetKey()
        if os.path.exists(_newJsonPath):
            # remove current settings
            for _key in self.ChildObjects:
                self.ChildObjects[_key].__del__()

            self.ChildObjects.clear()

            _newData = JsonToolKit.GetJsonAsDict(_newJsonPath)
            self.SetValue(_newData)

            self.MakeUI()
        else:
            print("Json File Does Not exist: ", self.GetKey())


def IsVector(_strut):
    if "R" and "G" and "B" in _strut:
        return True
    elif "r" and "g" and "b" in _strut:
        return True
    if "R" and "G" and "B" and "A" in _strut:
        return True
    elif "r" and "g" and "b" and "a" in _strut:
        return True
    elif "x" and "y" and "z" and "w" in _strut:
        return True
    elif "x" and "y" and "z" in _strut:
        return True
    elif "x" and "y" in _strut:
        return True
    elif "X" and "Y" and "Z" and "W" in _strut:
        return True
    elif "X" and "Y" and "Z" in _strut:
        return True
    elif "X" and "Y" in _strut:
        return True
    elif "max" and "min" in _strut:
        return True
    elif "Max" and "Min" in _strut:
        return True
    else:
        return False


def DelLayout(layout):
    try:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                DelLayout(child.layout())
    except:
        pass
