import UDP


udp = UDP.UDPServer()

while True:
    # msg = ["Hello", 1, 65]
    msg = input("Eneter Sumthin ")
    print(msg)
    msg = [msg]
    udp.SendMessage(msg)
