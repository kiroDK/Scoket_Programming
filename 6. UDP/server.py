import socket

localIP = "127.0.0.1"
localPort = 9999
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

s.bind((localIP, localPort))

print("UDP server up and listening")


while (True):
    bytesAddressPair = s.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    s.sendto(bytesToSend, address)