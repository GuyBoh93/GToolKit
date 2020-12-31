from Plugins.messaging import UDP
import time
from datetime import datetime

udp = UDP.UDPServer()

while True:
    msg = ["Hello", 1, 65]
    udp.SendMessage(msg)
    # print ("Message Sent: ", msg)
    # time.sleep(0.1)

