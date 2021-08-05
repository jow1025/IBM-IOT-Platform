import wiotp.sdk
import psutil
from time import sleep

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "hu5963", "typeId": "vDev", "deviceId": "dev01"},
    "auth": {"token": "passw0rd"},
}

def commandProcessor(cmd):
    print(cmd.data["d"])
    if cmd.data["d"]["info"]:
        data = {"d":{}}
        data["d"]["cpu_count"] = psutil.cpu_count()
        data["d"]["cpu_freq"] = psutil.cpu_freq().current
        data["d"]["memory"] = psutil.virtual_memory().total
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

while True:
    data = {"d":{}}
    data["d"]["cpu_usage"] = psutil.cpu_percent()
    data["d"]["mem_used"] = psutil.virtual_memory().used
    deviceCli.publishEvent("status", "json", data, qos=0)
    sleep(10)
