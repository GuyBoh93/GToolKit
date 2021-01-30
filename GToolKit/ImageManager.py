from PIL import Image
import os

### Resize images 
def SetImageRes(inPath, outPath="", size=[200, 200]):
    if isinstance(inPath, str):
        image = Image.open(inPath)
        image = image.resize((size[0], size[1]))
        if outPath == "":
            image.save(inPath)
        else:
            image.save(outPath)
    elif isinstance(inPath, list):
        for path in inPath:
            image = Image.open(path)
            image = image.resize((size[0], size[1]))
            if outPath == "":
                image.save(path)
            else:
                image.save(outPath + os.sep + os.path.basename(inPath))
            

def GetImageRes(path):
    image = Image.open(path)
    return image.size()


def RotateImageRight90(inPath, outPath=""):
    if outPath == "":
        outPath = inPath

    image = Image.open(inPath)
    image = image.rotate(90)
    image.save(outPath)


def RotateImageLeft90(inPath, outPath=""):
    if outPath == "":
        outPath = inPath
    image = Image.open(inPath)
    image = image.rotate(-90)
    image.save(outPath)

