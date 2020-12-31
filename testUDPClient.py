from Plugins.messaging import UDP
import time
from datetime import datetime


udp = UDP.UDPClient()

while True:
    startTime = datetime.now()
    print (str(datetime.now()))

    print (udp.GetLatestMessage())
 
    print (datetime.now() - startTime)
    time.sleep(5)