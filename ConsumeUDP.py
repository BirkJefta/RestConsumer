import requests
import json
import schedule
import time
from socket import *


hourNow = 0
RequestTime = str(hourNow)


def sendPriceCategory():
    serverPort = 12000
    broadcastAddress = ('255.255.255.255', serverPort)
    ServerSocket = socket(AF_INET, SOCK_DGRAM)
    ServerSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    URL = "google.com"
    #Response = requests.get(URL + "/" + RequestTime)
    Response = RequestTime
    ServerSocket.sendto(Response.encode(), broadcastAddress)



schedule.every(1).seconds.do(sendPriceCategory)


while True:
    schedule.run_pending()
    time.sleep(1)

#while True:
    
    #Til at kommunikerer med rest server
    #Response = requests.get(URL + "/" + RequestTime)
    #Response = "High"
    #print("RequestTime: ", (URL + "/" + RequestTime))

    #ServerSocket.sendto(Response.encode(), clientAddress)









