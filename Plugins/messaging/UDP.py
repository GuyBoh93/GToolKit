import socket
import time
from datetime import datetime
import select


class UDPServer():
    def __init__(self, ip="127.0.0.1", port=5005, prefix="---", messageFrom="GB"):
        self.port = port
        self.ip = ip
        self.prefix = str(prefix)
        self.messageFrom = str(messageFrom)
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

        # self.sock.bind((self.port, self.ip))

        def __del__(self):
            self.sock.close()
            print('Socket Clouded')

    def SendMessage(self, data=["Hello World"]):
        message = self._packMessage(data)
        message = message.encode('utf-8')

        self.sock.sendto(message, (self.ip, self.port))

    def _packMessage(self, messages=[]):
        # Added Star Messsgae and Time Stamp
        strMessage = self.messageFrom + self.prefix
        strMessage += str(datetime.now()) + self.prefix

        for meg in messages:
            strMessage += str(meg) + self.prefix

        return strMessage


class UDPClient():
    def __init__(self, ip="localhost", port=5005, prefix="---"):
        self.port = port
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

        self.sock.bind((self.ip, self.port))
        self.sock.setblocking(0)

    # ##########WIP#################

    #     while True:
    #         # try:
    #         #     data, addr = self.sock.recvfrom(
    #         #         1024)  # buffer size is 1024 bytes
    #         #     print("received message: %s" % data)
    #         # except BlockingIOError:
    #         #     print("Nothing")
    #         print (str(datetime.now()))
    #         # messages = self.GetAllMessages()
    #         print (self.GetLatestMessage())
    #         # for meg in messages:
    #         #     print(meg)
    #         # print(self.GetAllMessages())
    #         time.sleep(5)

    def FlushPort(self):
        self.GetAllMessages()

    def GetLatestMessage(self):
        messages = self.GetAllMessages()

        if len(messages) <= 0:
            return ""

        lastmsg = messages[len(messages)-1]
        return lastmsg

    def GetAllMessages(self):
        # Helper function to recv n bytes or return None if EOF is hit
        data = []
        while len(data) < 100000:
            try:
                meg, addr = self.sock.recvfrom(
                    1024)  # buffer size is 1024 bytes
                data.append(meg)
            except BlockingIOError:
                break

        return data
