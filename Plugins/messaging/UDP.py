import socket


class UDPServer():
    def __init__(self, ip="127.0.0.1", port=5005, prefix="GB---"):
        self.port = port
        self.ip = ip
        self.prefix = prefix
        self.sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

        # self.sock.bind((self.port, self.ip))

    def SendMessage(self, message="Hello World"): 
        # message = str.encode(message, 'utf-8')
        # message = str(message.encode())
        # message.upper()
        # message =  message.encode('utf-8')

        message = str(self.prefix) + str(message)
        message = message.encode('utf-8')
        # message = message.encode()

        self.sock.sendto(message, (self.ip, self.port))


class UDPClient():
    def __init__(self, ip="localhost", port=5005, prefix="GB---"):
        self.port = port
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

        self.sock.bind((self.ip, self.port))
        
    ##########WIP#################

        while True:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            print("received message: %s" % data)




