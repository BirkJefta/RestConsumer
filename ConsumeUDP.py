import requests
import json
from socket import *

# til at kommunikerer med rapberry pi

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAdress = ('', serverPort)
clientSocket.bind(serverAdress)
RequestTime = ""
URL = "google.com"

while True:
    message, clientAddress = clientSocket.recvfrom(2048)
    RequestTime = message.decode()
    #Til at kommunikerer med rest server
    #response = requests.get(URL + "/" + RequestTime)
    print("RequestTime: ", (URL + "/" + RequestTime))







