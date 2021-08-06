import wiotp.sdk
import psutil
from time import sleep
import Adafruit_DHT
dht_sensor=Adafruit_DHT.DHT11
pin=3
#humidity,temperature=Adafruit_DHT.read_retry(dht_sensor,pin)

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "vd6jub", "typeId": "vDev", "deviceId": "dht11"},
    "auth": {"token": "rla1rla1rla1"},
}

def commandProcessor(cmd):
    #node red(cloud)-> order-> rpi(doing)
    print(cmd.data["d"])
    if cmd.data["d"]["info"]:
        data = {"d":{}}
	
	# not define(cloud-> ibm iot-> device perform)

        #data["d"]["cpu_count"] = psutil.cpu_count()
        #data["d"]["cpu_freq"] = psutil.cpu_freq().current
        #data["d"]["memory"] = psutil.virtual_memory().total
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

while True:
    #do rpi-> ibm IOT event log
    data = {"d":{}}
    #data["d"]["cpu_usage"] = psutil.cpu_percent()
    #data["d"]["mem_used"] = psutil.virtual_memory().used
    humidity,temperature=Adafruit_DHT.read_retry(dht_sensor,pin)
    data["d"]["humidity"]=str(humidity)
    data["d"]["temperature"]=str(temperature)	
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("humidity: "+str(humidity)+"°C,Temperature: "+str(temperature)+"%")
    sleep(10)
