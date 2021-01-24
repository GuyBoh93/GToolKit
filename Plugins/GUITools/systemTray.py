from pystray import MenuItem as item
import pystray
from PIL import Image
import os
dir = os.path.dirname(os.path.realpath(__file__))


class SystemTray():
    def __init__(self, AppName="AppName" ,IconPath=""):

        image = Image.open(dir + os.sep + "icon.png")

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
        


if __name__ == "__main__":
    x = SystemTray()
