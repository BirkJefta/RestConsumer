import requests
import json
import schedule
import time
from socket import *

Zone = "East"
URL = "https://etrest-eaf7c7abe8hkdgh8.northeurope-01.azurewebsites.net/api/Elpris/"

#metoder
#sørger for at starte den timeplanlagte opgave
def RunSchedule():
    global runcount
    global jobref
    runcount = 0
    print("RunSchedule")
    ApiCall = requests.get(URL + "fromAPI")
    print("Response1: " + str(ApiCall))
    jobref = schedule.every().hour.do(hourlySendPrice)


    
# sørger for det maks er 24 timer herefter canceler den de forrige 24 timer hvorefter den starter forfra nederst
def hourlySendPrice():
    global runcount, jobref
    sendPriceCategory()
    runcount += 1
    print("runcount: " + str(runcount)) 
    if runcount == 24:
        schedule.cancel_job(jobref)
        


def sendPriceCategory():
    serverPort = 12000
    broadcastAddress = ('255.255.255.255', serverPort)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    CurrentTime = time.localtime().tm_hour
    RequestTime = str(CurrentTime)
    getURL = str(URL + Zone + "/" + RequestTime)
    response = requests.get(getURL)    
    print("Response: " + str(response))
    category = response.json().get("category")
    print("Price " + str(category))
    message = json.dumps(category) 
    print("Message: " + message)
    clientSocket.sendto(message.encode(), broadcastAddress)
    clientSocket.close()

#kør en gang hver dag.
#skal starte klokken midnat
schedule.every().day.at("00:00").do(RunSchedule)

#hoolder den tændt, så den kører schedule
while True:
    schedule.run_pending()
    time.sleep(1)










