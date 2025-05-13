import requests
import json
import schedule
import time
from socket import *

Zone = "Vest"
URL = "http://localhost:5029/api/Elpris/"


#sørger for at starte den timeplanlagte opgave
def RunSchedule():
    global runcount
    global jobref
    runcount = 0
    print("RunSchedule")
    #response = requests.get("https://etrest-eaf7c7abe8hkdgh8.northeurope-01.azurewebsites.net/api/Elpris/fromAPI/Vest")
    #response = requests.get("https://etrest-eaf7c7abe8hkdgh8.northeurope-01.azurewebsites.net/api/Elpris/fromAPI/Øst")
    response = requests.get("http://localhost:5029/api/Elpris/fromAPI/Vest")
    print("Response1: " + str(response))
    jobref = schedule.every().second.do(hourlySendPrice)
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
    hourNow = CurrentTime
    RequestTime = str(hourNow)
    #URL = "https://etrest-eaf7c7abe8hkdgh8.northeurope-01.azurewebsites.net/api/Elpris/" 
    URL = "http://localhost:5029/api/Elpris/fromAPI/Vest"
   #Response = requests.get(URL + Zone + "/" + RequestTime)
    Response = requests.get("http://localhost:5029/api/Elpris/Vest/14")
    print("Response: " + str(Response))
    data = Response.json()
    EnergyPrice = {
    "id": data.get("id"),
    "dkK_per_kWh": data.get("dkK_per_kWh"),
    "time_start": data.get("time_start"),
    "Category": data.get("Category"),
    }
    print("EnergyPrice: " + str(EnergyPrice))
    jsonCategory = json.dumps(EnergyPrice["dkK_per_kWh"])
    print("jsonCategory: " + str(jsonCategory))
    #clientSocket.sendto(jsonCategory, broadcastAddress)
    clientSocket.close()


#skal starte klokken midnat
schedule.every().day.at("14:37").do(RunSchedule)


while True:
    schedule.run_pending()
    time.sleep(1)










