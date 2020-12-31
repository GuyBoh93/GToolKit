from Plugins.messaging import UDP
import time

udp = UDP.UDPServer()

while True:
    msg = "ABC"
    udp.SendMessage(msg)
    print ("Message Sent: ", msg)
    # time.sleep(0.01)

