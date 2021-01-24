import socket
import time
from datetime import datetime
import select


class UDPServer():
    def __init__(self, ip="localhost", port=5005, prefix="---", messageFrom="GB"):
        self.port = port
        self.ip = ip
        self.prefix = str(prefix)
        self.messageFrom = str(messageFrom)
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
       

        # self.sock.settimeout(0.2)

    def __del__(self):
        self.sock.close()
        print('Socket Clouded')

    def SendMessage(self, data=["Hello World"]):
        message = self._packMessage(data)
        message = message.encode('utf-8')

        self.sock.sendto(message, (self.ip, self.port))

    def _packMessage(self, messages=[]):

        strMessage = self.messageFrom + self.prefix
        strMessage += str(datetime.now()) + self.prefix

        for meg in messages:
            strMessage += str(meg) + self.prefix

        return strMessage


class UDPClient():
    def __init__(self, ip="localhost", port=5005, prefix="---", messageFrom="GB"):
        self.port = port
        self.ip = ip
        self.messageFrom = messageFrom
        self.prefix = prefix
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.sock.bind((self.ip, self.port))
        self.sock.setblocking(0)

    def __del__(self):
        self.sock.close()
        print('Socket Clouded')

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
                meg = str(meg, 'UTF-8')
                splitmessage = meg.split(self.prefix)
                if str(splitmessage[0]) in self.messageFrom:
                    data.append(meg)
            except BlockingIOError:
                break

        return data


class UDPSender(UDPServer):
    pass


class UDPReciver(UDPClient):
    pass


class UDPBroacasting():
    def __init__(self, port=9, prefix="---", messageFrom="GB"):
        self.sender = UDPSender(
            ip="192.168.0.255", port=port, prefix=prefix, messageFrom=messageFrom)
        self.sender.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.reciver = UDPReciver(
        #     ip="", port=port, prefix=prefix, messageFrom=messageFrom)
        # self.reciver.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def BrocastMessgae(self, data=["Hello World"]):
        self.sender.SendMessage(data)

    def SendMessgae(self, data=["Hello World"]):
        self.sender.SendMessage(data)

    def GetAllMessages(self):
        return self.reciver.GetAllMessages()

    def GetLatestMessage(self):
        return self.reciver.GetLatestMessage()

    def FlushPort(self):
        self.reciver.FlushPort()


if __name__ == "__main__":
    x = UDPBroacasting()

    while True:
        x.SendMessgae()
        # mesg = x.GetAllMessages()

        # for i in mesg:
        #     print(i)
        print("*")
        time.sleep(2)
