import requests
import json
import schedule
import time
from socket import *

Zone = "Vest"
URL = "https://etrest-eaf7c7abe8hkdgh8.northeurope-01.azurewebsites.net/api/Elpris/"

#metoder
#sørger for at starte den timeplanlagte opgave
def RunSchedule():
    global runcount
    global jobref
    runcount = 0
    print("RunSchedule")
    VestResponse = requests.get(URL + "fromAPI/Vest")
    ØstResponse = requests.get(URL + "fromAPI/Øst")
    print("Response1: " + str(VestResponse))
    jobref = schedule.every().hour.do(hourlySendPrice)
# sørger for det maks er 24 timer herefter canceler den de forrige 24 timer hvorefter den starter forfra nederst
def hourlySendPrice():
    global runcount, jobref
    sendPriceCategory()
    runcount += 1
    print("runcount: " + str(runcount)) 
    if runcount > 24:
        schedule.cancel_job(jobref)
        


def sendPriceCategory():
    serverPort = 12000
    broadcastAddress = ('255.255.255.255', serverPort)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    CurrentTime = time.localtime().tm_hour
    RequestTime = str(CurrentTime)
    getURL = URL + Zone + "/" + RequestTime
    response = requests.get(getURL)
    print("Response: " + str(response))
    #Skal laves om til category når den ikke er null mere og der er lavet en funktion til at udregne den
    dkK_per_kWh = response.json().get("dkK_per_kWh")
    print("Price " + str(dkK_per_kWh))
    message = json.dumps(dkK_per_kWh)
    print("Message: " + message)
    clientSocket.sendto(message.encode(), broadcastAddress)
    clientSocket.close()

#kør en gang hver dag.
#skal starte klokken midnat
schedule.every().day.at("14:37").do(RunSchedule)

#hoolder den tændt, så den kører schedule
while True:
    schedule.run_pending()
    time.sleep(1)










