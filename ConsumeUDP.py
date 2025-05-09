import requests
import json
import schedule
import time
from socket import *



def RunSchedule():
    schedule.every().second.do(sendPriceCategory)


def sendPriceCategory():
    serverPort = 12000
    broadcastAddress = ('255.255.255.255', serverPort)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    CurrentTime = time.localtime().tm_hour
    hourNow = CurrentTime
    RequestTime = str(hourNow)
    URL = "google.com"
    #Response = requests.get(URL + "/" + RequestTime)
    Response = "high"
    clientSocket.sendto(Response.encode(), broadcastAddress)
    clientSocket.close()



schedule.every().day.at("13:23").do(RunSchedule)


while True:
    schedule.run_pending()
    time.sleep(1)

#while True:
    
    #Til at kommunikerer med rest server
    #Response = requests.get(URL + "/" + RequestTime)
    #Response = "High"
    #print("RequestTime: ", (URL + "/" + RequestTime))

    #ServerSocket.sendto(Response.encode(), clientAddress)









