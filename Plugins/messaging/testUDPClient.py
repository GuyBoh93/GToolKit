from Plugins.messaging import UDP
import time
from datetime import datetime


udp = UDP.UDPClient()

while True:
    # startTime = datetime.now()
    # print (str(datetime.now()))
    message = udp.GetLatestMessage()
    if len(message) > 0:
        print (message)
 
    # print (datetime.now() - startTime)
    time.sleep(0.1)