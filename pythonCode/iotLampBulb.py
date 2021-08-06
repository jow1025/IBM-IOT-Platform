<<<<<<< HEAD
import wiotp.sdk
from utils import bulb

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "due986", "typeId": "vDev", "deviceId": "vLamp"},
    "auth": {"token": "passw0rd"},
}

lamp = 'off'

def commandProcessor(cmd):
    global lamp
    if cmd.data["d"]["lamp"]:
        data = {}
        if cmd.data["d"]["lamp"] == "on":
            lamp = 'on'
            bulb.bulbOn()
            data = {"d" : {"lamp" : "on"}}
        else:
            lamp = 'off'
            bulb.bulbOff()
            data = {"d" : {"lamp" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"lamp": lamp}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + lamp)
    bulb.after(3000, periodicPublish)

bulb.after(3000, periodicPublish)
bulb.mainloop()
=======
import wiotp.sdk
from utils import bulb

# ibm iot platform device credential here
deviceOptions = {
    "identity": {"orgId": "due986", "typeId": "vDev", "deviceId": "vLamp"},
    "auth": {"token": "passw0rd"},
}

lamp = 'off'

def commandProcessor(cmd):
    global lamp
    if cmd.data["d"]["lamp"]:
        data = {}
        if cmd.data["d"]["lamp"] == "on":
            lamp = 'on'
            bulb.bulbOn()
            data = {"d" : {"lamp" : "on"}}
        else:
            lamp = 'off'
            bulb.bulbOff()
            data = {"d" : {"lamp" : "off"}}
        deviceCli.publishEvent("status", "json", data, qos=0)

deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor
deviceCli.connect()

def periodicPublish():
    data = {"d":{"lamp": lamp}}
    deviceCli.publishEvent("status", "json", data, qos=0)
    print("        Periodic update : Lamp is " + lamp)
    bulb.after(3000, periodicPublish)

bulb.after(3000, periodicPublish)
bulb.mainloop()
>>>>>>> a406e59877fd3017b5c5d39c9ee713d9a18c3f59
