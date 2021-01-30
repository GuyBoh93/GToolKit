import json 
import os

def GetJsonAsDict(_Location):
    if os.path.isfile(_Location):
        jsonFile = open(_Location, "r", encoding="utf-8")
        jsonData = json.load(jsonFile)
        jsonFile.close()
        return jsonData
    else:
        print("ERROR: Could not find:" + _Location)


def SaveDictToJson(_saveLocation, _fileName, _jsonData):
    _file = open(str(_saveLocation + os.sep) +
                 str(_fileName), "w", encoding="utf-8")
    json.dump(_jsonData, _file, indent=4)

    _file.close()
    print(str(_saveLocation + os.sep) + str(_fileName))

    print("Json Saved to: " + _saveLocation + os.sep + _fileName)

def SaveDictToJsonFullPath(_fullPath, _jsonData):
    _file = open(str(_fullPath), "w", encoding="utf-8")
    json.dump(_jsonData, _file, indent=4)

    _file.close()
    print(_fullPath)

    print("Json Saved to: " + _fullPath)


def DictToSting(_dict):
    _string = json.dumps(_dict)
    return _string


def GetAllJsonPathsCalled(_path, _fileName):
    filesPaths = []

    for (dirpath, dirnames, filenames) in os.walk(_path):
        for fineName in filenames:
            if _fileName in fineName:
                filesPaths.append(dirpath + os.sep + fineName)

    return filesPaths

def GetAllJsonPaths(self, _path):
    filesPaths = []

    for (dirpath, dirnames, filenames) in os.walk(_path):
        for fineName in filenames:
            if fineName.endswith('.json'):
                filesPaths.append(dirpath + os.sep + fineName)

    return filesPaths



