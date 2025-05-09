import requests
import json
from socket import *

# til at kommunikerer med rapberry pi

serverPort = 12000
ServerSocket = socket(AF_INET, SOCK_DGRAM)
serverAdress = ('', serverPort)
ServerSocket.bind(serverAdress)
RequestTime = ""
URL = "google.com"

while True:
    Message, clientAddress = ServerSocket.recvfrom(2048)
    RequestTime = Message.decode()
    #Til at kommunikerer med rest server
    #Response = requests.get(URL + "/" + RequestTime)
    Response = "High"
    print("RequestTime: ", (URL + "/" + RequestTime))

    ServerSocket.sendto(Response.encode(), clientAddress)







