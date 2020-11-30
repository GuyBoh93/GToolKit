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