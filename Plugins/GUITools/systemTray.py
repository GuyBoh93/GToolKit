from pystray import MenuItem as item
import pystray
from PIL import Image
import os
dir = os.path.dirname(os.path.realpath(__file__))

currentFile = __file__  # May be 'my_script', or './my_script' or
# '/home/user/test/my_script.py' depending on exactly how
# the script was run/loaded.
realPath = os.path.realpath(currentFile)  # /home/user/test/my_script.py
dir = os.path.dirname(realPath)


class SystemTray():
    def __init__(self, AppName="AppName", IconPath=""):
        if IconPath == "":
            image = Image.open(dir + os.sep + "icon.png")
        else:
            image = Image.open(IconPath)

        self.CreateTrayMenu()

        self.icon = pystray.Icon("name", image, str(AppName), self.menu)
        self.icon.run()

    def CreateTrayMenu(self):
        self.menu = (item('Info', self.OpenInfo),
                     item('Open Gui', self.OpenGui),
                     item('- - - -', None),
                     item('Quit', self.Quit)
                     )

    def OpenGui(self):
        print("GUI Open")

    def OpenInfo(self):
        print("App Info")

    def Quit(self):
        self.icon.stop()


class test(SystemTray):
    def __init__(self):
        SystemTray.__init__(self, AppName="Hi")


if __name__ == "__main__":
    # x = SystemTray()
    x = test()
