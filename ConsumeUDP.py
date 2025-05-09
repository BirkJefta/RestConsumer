import requests
import json
import schedule
import time
from socket import *



def RunSchedule():
    global runcount
    global jobref
    runcount = 0
    jobref = schedule.every().second.do(hourlySendPrice)

def hourlySendPrice():
    global runcount, jobref
    sendPriceCategory()
    runcount += 1
    print("runcount: " + str(runcount))
    if runcount > 10:
        schedule.cancel_job(jobref)
        


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



schedule.every().day.at("14:01").do(RunSchedule)


while True:
    schedule.run_pending()
    time.sleep(1)










