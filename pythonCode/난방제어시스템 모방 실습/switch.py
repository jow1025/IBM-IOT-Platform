from gpiozero import LED
import wiotp.sdk
from time import sleep

switch=LED(2)
switch.off()
# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "aua984", "typeId": "vDev", "deviceId": "switch"},
    "auth": {"token": "password"},
}

switch_state = 'off'

def commandProcessor(cmd):
    global switch_state
    if cmd.data["d"]["switch_state"]:
        data = {}
        if cmd.data["d"]["switch_state"] == "on":
            switch_state = 'on'
            switch.on()
            print("Switch is On")
            data = {"d" : {"switch_state" : "on"}}
        else:
            switch_state = 'off'
            switch.off()
            print("Switch is Off")
            data = {"d" : {"switch_state" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)
        
deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"switch_state": switch_state}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Switch is " + switch_state)

while True:
    periodicPublish()
    sleep(10)
