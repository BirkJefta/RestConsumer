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
    message, clientAddress = ServerSocket.recvfrom(2048)
    RequestTime = message.decode()
    #Til at kommunikerer med rest server
    #response = requests.get(URL + "/" + RequestTime)
    Response = "Høj"
    print("RequestTime: ", (URL + "/" + RequestTime))

    ServerSocket.sendto(Response.encode(), clientAddress)







